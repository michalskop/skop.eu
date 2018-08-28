# prepare data into json

import csv
import json

path = "/home/michal/dev/skola/dotaznik/results/teachers/"

with open(path + "questions.json") as fin:
    questions = json.load(fin)

with open(path + "scales.json") as fin:
    scales = json.load(fin)

data = []
for q in questions:
    item = q
    try:
        scale = scales[q['scale']]
        item['all'] = [0] * len(scale)
        data.append(q)
    except Exception:
        nothing = None

with open(path + "spokojenost_ucitelu_2018.csv") as fin:
    dr = csv.DictReader(fin)
    for row in dr:
        for q in data:
            answer = row[q['question']]
            scale = scales[q['scale']]
            i = 0
            for item in scale:
                if item['value'] == answer:
                    q['all'][i] += 1
                i += 1

with open(path + "data.json", "w") as fout:
    json.dump(data, fout, ensure_ascii=False)
