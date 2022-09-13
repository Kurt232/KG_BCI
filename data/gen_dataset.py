import json
# import jieba

def get_pose(text, E_name):
    result = []
    pose_1 = text.find(E_name)
    pose_2 = pose_1+len(E_name)-1
    result.append(pose_1)
    result.append(pose_2)
    return result

with open('./data/raw_train.txt', 'r') as fp , \
    open('./data/bci_train.txt', "w+") as fp1:
    # line = fp.readline()#skip
    rel2id = {}
    cnt = 0
    # line = fp.readline().split()
    # print(jieba.lcut(line[1], cut_all = False))
    while True:

        line = fp.readline()

        if not line:
            break
        
        _, E1, E2, text, rel = line.split() ##句子id 实体1 实体2 句子 关系

        sentence = {}
        # sentence['token'] = jieba.lcut(line[3], cut_all=False)
        sentence["token"] = list(text)
        h = {}
        h["name"] = E1
        h["pos"] = get_pose(text, E1) 
        sentence["h"] = h
        t = {}
        t["name"] = E2
        t["pos"] = get_pose(text, E2)
        sentence["t"] = t
        sentence["relation"] = rel

        if sentence['relation'] not in rel2id.keys():
            rel2id[sentence['relation']] = cnt
            cnt = cnt + 1

        s = json.dumps(sentence, ensure_ascii=False)
        fp1.write(s + "\n")

with open('./data/bci_rel2id.json', 'w') as fp:
    json.dump(rel2id, fp, ensure_ascii=False)

