# calculate ecological inference

import csv
import numpy
import rpy2.robjects as robjects
r = robjects.r

path = "/home/michal/dev/prechody/2013-2014/"

robjects.globalenv["par_input"] = path + "data_filtered_random.csv"
try:
    r.source("ei.r")
    with open(path + "matp_filtered.csv", "w") as fout:
        csvw = csv.writer(fout)
        for row in numpy.array(robjects.globalenv['matp']):
            csvw.writerow(list(row))
    with open(path + "matn_filtered.csv", "w") as fout:
        csvw = csv.writer(fout)
        for row in numpy.array(robjects.globalenv['mat_ave']):
            csvw.writerow(list(row))
except Exception:
    print("skipping")
