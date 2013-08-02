import csv
import numpy as np
import pylab

data = csv.reader(open('qc.csv', 'r'))
next(data, None) # skip the headers 

qc_data = []

for row in data:
    qc_data.append(float(row[1]))

pylab.title('Order life in QC in hours', fontsize=20)
pylab.boxplot(qc_data)
pylab.show()
