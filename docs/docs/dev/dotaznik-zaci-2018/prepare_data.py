# prepare data into json

import csv
import json

path = "/home/michal/dev/skola/dotaznik/results/"

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
        item['classes'] = [
            {"class": 6, "values": [0] * len(scale)}, {"class": 7, "values": [0] * len(scale)}, {"class": 8, "values": [0] * len(scale)}, {"class": 9, "values": [0] * len(scale)}
        ]
        data.append(q)
    except Exception:
        nothing = None

with open(path + "spokojenost_zaku_2018.csv") as fin:
    dr = csv.DictReader(fin)
    for row in dr:
        clss = int(row['Do jaké třídy chodíš?'])
        for q in data:
            answer = row[q['question']]
            scale = scales[q['scale']]
            i = 0
            for item in scale:
                if item['value'] == answer:
                    q['all'][i] += 1
                    q['classes'][clss - 6]['values'][i] += 1
                i += 1

with open(path + "data.json", "w") as fout:
    json.dump(data, fout, ensure_ascii=False)
