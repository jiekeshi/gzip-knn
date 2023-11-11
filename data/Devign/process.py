import csv
import json

from tqdm import tqdm

with open("test.jsonl") as f:
    test = [json.loads(line) for line in f.readlines()]

with open("test.csv", "w") as f:
    writer = csv.writer(f)
    for item in tqdm(test):
        writer.writerow([item["target"], "", item["func"].replace("\n", " ").replace("\r", " ").replace("\t", " ").strip()])

with open("train.jsonl") as f:
    train = [json.loads(line) for line in f.readlines()]

with open("train.csv", "w") as f:
    writer = csv.writer(f)
    for item in tqdm(train):
        writer.writerow([item["target"], "", item["func"].replace("\n", " ").replace("\r", " ").replace("\t", " ").strip()])

# url_to_code = {}

# with open("data.jsonl") as f:
#     for line in f:
#         line = line.strip()
#         js = json.loads(line)
#         url_to_code[js["idx"]] = js["func"]

# data = []
# with open("label_train.txt") as f:
#     for line in f:
#         line = line.strip()
#         url1, url2, label, pred = line.split("\t")
#         if url1 not in url_to_code or url2 not in url_to_code:
#             continue
#         if pred == "0":
#             pred = 0
#         elif pred == "1":
#             pred = 1
#         else:
#             pred = -1

#         if label == "0":
#             label = 0
#         elif label == "1":
#             label = 1
#         elif label == "-1":
#             label = pred
#             # label = -1

#         data.append((url1, url2, label, pred, url_to_code))

# with open("train.csv", "w") as f:
#     writer = csv.writer(f)
#     for item in tqdm(data):
#         writer.writerow([item[2], "", url_to_code[item[0]].replace("\n", " ").replace("\r", " ").replace("\t", " ").strip() + " " + url_to_code[item[1]].replace("\n", " ").replace("\r", " ").replace("\t", " ").strip()])

# data = []
# with open("test_sampled.txt") as f:
#     for line in f:
#         line = line.strip()
#         url1, url2, label = line.split("\t")
#         if url1 not in url_to_code or url2 not in url_to_code:
#             continue
#         if label == "0":
#             label = 0
#         elif label == "1":
#             label = 1

#         data.append((url1, url2, label, url_to_code))

# with open("test.csv", "w") as f:
#     writer = csv.writer(f)
#     for item in tqdm(data):
#         writer.writerow([item[2], "", url_to_code[item[0]].replace("\n", " ").replace("\r", " ").replace("\t", " ").strip() + " " + url_to_code[item[1]].replace("\n", " ").replace("\r", " ").replace("\t", " ").strip()])