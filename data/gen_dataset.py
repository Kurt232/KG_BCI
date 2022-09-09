import json
import jieba

with open('./data/raw_train.txt', 'r') as fp , \
    open('./data/bci_train.txt', "w+") as fp1:
    # line = fp.readline()#skip
    relation = {}
    cnt = 0
    # line = fp.readline().split()
    # print(jieba.lcut(line[1], cut_all = False))
    while True:

        line = fp.readline()

        if not line:
            break
        
        line = line.split() ##句子id 实体1 实体2 句子 关系

        sentence = {}
        sentence['token'] = jieba.lcut(line[3], cut_all=False)
        h = {}
        name = jieba.lcut(line[1], cut_all=False)
        assert len(name)>= 1
        h['name'] = name[0]
        for i in range(1, len(name)):
            h['name'] = h['name'] + " " + name[i]
        
        for ix in range(0, len(sentence['token'])-len(name)):
            f = True
            for iy, vy in enumerate(name):
                if vy != sentence['token'][ix+iy]:
                    f = False
                    break
            
            if f:
                h['pos'] = [ix, ix + len(name)]
        sentence['h'] = h

        t = {}
        name = jieba.lcut(line[2], cut_all=False)
        assert len(name)>= 1
        t['name'] = name[0]
        for i in range(1, len(name)):
            t['name'] = t['name'] + " " + name[i]
        
        for ix in range(0, len(sentence['token'])-len(name)):
            f = True
            for iy, vy in enumerate(name):
                if vy != sentence['token'][ix+iy]:
                    f = False
                    break
            
            if f:
                t['pos'] = [ix, ix + len(name)]
                break

        sentence['t'] = t

        relation_cut = jieba.lcut(line[4], cut_all=False)
        assert len(relation_cut) >= 1
        sentence['relation'] = relation_cut[0]
        for i  in range(1, len(relation_cut)):
            sentence['relation'] = sentence['relation'] + " " + relation_cut[i]
        
        if sentence['relation'] not in relation.keys():
            relation[sentence['relation']] = cnt
            cnt = cnt + 1

        s = json.dumps(sentence, ensure_ascii=False)
        fp1.write(s + "\n")

with open('./data/bci_rel2id.json', 'w') as fp:
    print(relation)
    json.dump(relation, fp)

