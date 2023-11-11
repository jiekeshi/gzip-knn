"""
This needs to import "data" from https://github.com/bazingagin/npc_gzip

Save all datasets as pickle files to $outdir/$name.pkl

 data['train_data'] : [str]
 data['test_data'] : [str]
 data['train_labels'] : ndarray (n_train,) dtype=uint32
 data['test_labels']  : ndarray (n_test,)  dtype=uint32

"""
# from data import (
#     load_kinnews,
#     load_kirnews,
#     load_filipino,
#     load_swahili,
#     load_20news,
#     )
# import torchtext.datasets
import os
import pickle
import numpy as np
import argparse
from tqdm import tqdm
#needed to add for SogouNews dataset:
import sys
import csv
print("SET csv.field_size_limit:", sys.maxsize)
csv.field_size_limit(sys.maxsize)


# def load_torch(name):
#     Cls = getattr(torchtext.datasets,name)
#     return Cls(root="data")

import json
def load_devign(di):
    def process(d):
        ds = []
        with open(d) as f:
            ds = [json.loads(line) for line in f.readlines()]
        dss = []
        for pair in ds:
            label = pair['target']
            text = pair['func']
            dss.append((label, text))
        return dss
    train_dir = os.path.join(di, 'train.jsonl')
    test_dir = os.path.join(di, 'test.jsonl')
    train_ds, test_ds = process(train_dir), process(test_dir)
    return train_ds, test_ds

def main():
    # """
    # """
    # parser = argparse.ArgumentParser()

    # parser.add_argument(
    #     '--outdir',
    #     help = "write $outdir/$name.pkl")

    # args = parser.parse_args()
    # outdir = args.outdir

    # # construct list of (name, lambda : data)
    # DSS = []
    # for name in (
    #         "AG_NEWS",
    #         "DBpedia",
    #         "YahooAnswers",
    # ):
    #     DSS.append((name,lambda : load_torch(name)))

    # DSS.append(('20News', load_20news))
    # #ohsumed
    # #R8
    # #R52

    # DSS.extend([
    #     ('kinnews', load_kinnews),
    #     ('kirnews', load_kirnews),
    #     ('filipino',load_filipino),
    #     ('swahili', load_swahili),
    # ])
    # name = "SogouNews"
    # DSS.append((name,lambda : load_torch(name)))


    # for name,fn in DSS:

    #     tr,te = fn()


    # tr,te = load_devign("data/Devign")

    url_to_code = {}

    with open("data/BigCloneBench/data.jsonl") as f:
        for line in f:
            line = line.strip()
            js = json.loads(line)
            url_to_code[js["idx"]] = js["func"]

    data = []
    with open("data/BigCloneBench/train_sampled.txt") as f:
        for line in f:
            line = line.strip()
            url1, url2, label = line.split("\t")
            if url1 not in url_to_code or url2 not in url_to_code:
                continue

            if label == "0":
                label = 0
            elif label == "1":
                label = 1

            data.append((url1, url2, label))

    tr = []
    for item in tqdm(data):
        tr.append((item[2], url_to_code[item[0]].replace("\n", " ").replace("\r", " ").replace("\t", " ").strip() + " " + url_to_code[item[1]].replace("\n", " ").replace("\r", " ").replace("\t", " ").strip()))

    data = []
    with open("data/BigCloneBench/test_sampled.txt") as f:
        for line in f:
            line = line.strip()
            url1, url2, label = line.split("\t")
            if url1 not in url_to_code or url2 not in url_to_code:
                continue
            if label == "0":
                label = 0
            elif label == "1":
                label = 1

            data.append((url1, url2, label))

    te = []
    for item in tqdm(data):
        te.append((item[2], url_to_code[item[0]].replace("\n", " ").replace("\r", " ").replace("\t", " ").strip() + " " + url_to_code[item[1]].replace("\n", " ").replace("\r", " ").replace("\t", " ").strip()))

    tr = list(tr)
    te = list(te)

    # outfile = os.path.join("data", "Devign.pkl")
    outfile = os.path.join("data", "BigCloneBench.pkl")

    dtype = 'uint32'
    print("tr,te:", (len(tr), len(te)))
    pickle.dump({
        'train_data': [t for (l,t) in tr],
        'test_data':  [t for (l,t) in te],
        'train_labels': np.array([l for (l,t) in tr],dtype),
        'test_labels':  np.array([l for (l,t) in te],dtype),
    }, open(outfile,'wb'))
    print("wrote:",outfile)

if __name__ == "__main__":
    main()
