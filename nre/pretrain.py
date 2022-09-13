from . import encoder
from . import model
from . import framework
import torch
import os
import sys
import json
import numpy as np
import logging

default_root_path = os.path.join(os.getenv('HOME'), '.nre')

def check_root(root_path=default_root_path):
    if not os.path.exists(root_path):
        os.mkdir(root_path)
        os.mkdir(os.path.join(root_path, 'benchmark'))
        os.mkdir(os.path.join(root_path, 'pretrain'))
        os.mkdir(os.path.join(root_path, 'pretrain/nre'))

def get_model(model_name, root_path=default_root_path):
    check_root()
    ckpt = os.path.join(root_path, 'pretrain/nre/' + model_name + '.pth.tar')
    if model_name == 'test_chinese_bert_softmax':
        rel2id = json.load(open(os.path.join(root_path, 'benchmark/test_chinese/test_chinese_rel2id.json')))
        sentence_encoder = encoder.BERTEncoder(
            max_length=80, pretrain_path=os.path.join(root_path, 'pretrain/chinese_wwm_pytorch'))
        m = model.SoftmaxNN(sentence_encoder, len(rel2id), rel2id)
        m.load_state_dict(torch.load(ckpt)['state_dict'])
        return m
    else:
        raise NotImplementedError
