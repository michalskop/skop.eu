# join the 2013 and 2014 data for ei
import csv
import random

path = "/home/michal/dev/prechody/2013-2014/"


def n2(n):
    if n < 10:
        return "0" + str(n)
    else:
        return str(n)


def n(s):
    if s == '':
        return 0
    else:
        return int(s)


# data rows
d = {
    '2013': {},
    '2014': {}
}
# stations in municipality for matching in changed numbering municipality
stations = {
    '2013': {},
    '2014': {}
}
# selected data, filtered out 6 % of polling stations
data = {}
for y in d:
    with open(path + "data_" + y + ".csv") as fin:
        dr = csv.DictReader(fin)
        for row in dr:
            try:
                stations[y][row['OBEC']]
            except Exception:
                stations[y][row['OBEC']] = []
                d[y][row['OBEC']] = {}
            stations[y][row['OBEC']].append(row['OKRSEK'])
            d[y][row['OBEC']][row['OKRSEK']] = row

for muni in d['2014']:
    same = True
    for okr in stations['2014'][muni]:
        try:
            d['2013'][muni][okr]
        except Exception:
            same = False
    if same:
        data[muni] = {}
        for okr in stations['2014'][muni]:
            data[muni][okr] = {}
            data[muni][okr]['2013'] = d['2013'][muni][okr]
            data[muni][okr]['2014'] = d['2014'][muni][okr]
    else:
        try:
            if len(stations['2013'][muni]) == len(stations['2014'][muni]):
                data[muni] = {}
                for i in range(0, len(stations['2013'][muni])):
                    o2014 = stations['2014'][muni][i]
                    o2013 = stations['2013'][muni][i]
                    data[muni][o2014] = {}
                    data[muni][o2014]['2013'] = d['2013'][muni][o2013]
                    data[muni][o2014]['2014'] = d['2014'][muni][o2014]
            else:
                print(muni, len(stations['2014'][muni]), '::not the same number or stations')
        except Exception:
            print(muni, len(stations['2014'][muni]), '::not in 2013')

# filter parties, randomly select some districts to be able to perfomr EI
parties = {
    # '2013': [1, 3, 4, 6, 11, 17, 19, 20],
    '2014': [0, 1, 3, 9, 18, 19, 24, 25],
    '2013': [1, 3, 4, 6, 11, 17, 19, 20]
}

with open(path + "data_filtered_random.csv", "w") as foutR:
    select = 1  # 0.25
    header = []
    for k in parties['2013']:
        header.append('A' + str(k))
    header.append('A997')
    header.append('A998')
    header.append('A999')
    for k in parties['2014']:
        header.append('B' + str(k))
    header.append('B997')
    header.append('B998')
    header.append('B999')
    drR = csv.DictWriter(foutR, header)
    drR.writeheader()
    with open("data_filtered.csv", "w") as fout:
        dr = csv.DictWriter(fout, header)
        dr.writeheader()
        for muni in data:
            for okr in data[muni]:
                row = {}
                for y in parties:
                    if y == '2013':
                        code = 'A'
                    else:
                        code = 'B'
                    s = 0
                    for k in parties[y]:
                        try:
                            num = round(float(data[muni][okr][y]['HLASY_' + n2(k)]))
                        except Exception:
                            num = 0
                        s += num
                        row[code + str(k)] = num
                    row[code + '997'] = int(data[muni][okr][y]['HLASY']) - s
                    row[code + '999'] = int(data[muni][okr][y]['VOLICI']) - int(data[muni][okr][y]['HLASY'])

                if int(data[muni][okr]['2013']['VOLICI']) >= int(data[muni][okr]['2014']['VOLICI']):
                    row['B998'] = round(float(data[muni][okr]['2013']['VOLICI'])) - int(data[muni][okr]['2014']['VOLICI'])
                    row['A998'] = 0
                else:
                    row['A998'] = int(data[muni][okr]['2014']['VOLICI']) - round(float(data[muni][okr]['2013']['VOLICI']))
                    row['B998'] = 0
                if (1.25 * int(data[muni][okr]['2013']['VOLICI']) >= int(data[muni][okr]['2014']['VOLICI'])) and (0.8 * round(float(data[muni][okr]['2013']['VOLICI'])) <= int(data[muni][okr]['2014']['VOLICI'])):
                    dr.writerow(row)
                    if random.random() < select:
                        drR.writerow(row)
