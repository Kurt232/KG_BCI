import json

with open("./data/middle.json", "r") as fp:
    data = json.load(fp)
    fp.close()

with open("./data/train.txt", "a") as fp:
    id = 0
    for e in data:
        id = id + 1
        string = str(id) + " " + e['E1'] + " " + e['E2'] + " " + e['triple'][0] + e['triple'][1] + e['triple'][2] + " " + e['triple'][1] + '\n'
        fp.writelines([string])

