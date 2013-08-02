import csv
import numpy as np
import pylab

data = csv.reader(open('fitting.csv', 'r'))
next(data, None) # skip the headers 

fitting_data = []

for row in data:
    fitting_data.append(float(row[1]))

pylab.title('Order life in fitting in hours', fontsize=20)
pylab.boxplot(fitting_data)
pylab.show()
