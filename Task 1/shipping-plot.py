import csv
import numpy as np
import pylab

data = csv.reader(open('shipping.csv', 'r'))
next(data, None) # skip the headers 

ship_data = {}

for row in data:
    carrier = row[1]
    if carrier in ship_data:
        ship_data[carrier].append(float(row[2]))
    else:
        ship_data[carrier] = [float(row[2])]

data = [val for val in ship_data.values()]
pylab.title('Delivery time in hours by delivery medium', fontsize=20)
pylab.boxplot(data)
pylab.xticks([(i + 1) for i in range(len(ship_data.values()))], \
             ['%s' % i for i in ship_data.keys()])
pylab.show()
