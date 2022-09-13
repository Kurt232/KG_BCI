# import opennre

# if __name__ == "__main__":
#     model = opennre.get_model('wiki80_cnn_softmax')
#     model = model.cuda()
#     print(model.infer({'text': 'He was the son of Máel Dúin mac Máele Fithrich, and grandson of the high king Áed Uaridnach (died 612).', 'h': {'pos': (18, 46)}, 't': {'pos': (78, 91)}}))

from nre.pretrain import get_model

if __name__ == "__main__":
    model = get_model('chinese_wwm_ext_pytorch')
    model = model.cuda()
    with open("./data/text.txt") as fp:
        line = fp.readline()
        print(model.infer(line))