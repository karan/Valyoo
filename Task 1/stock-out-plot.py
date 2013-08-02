import csv
import numpy as np
import pylab

data = csv.reader(open('stock-out.csv', 'r'))
next(data, None) # skip the headers 

stock_out_data = []

for row in data:
    stock_out_data.append(float(row[1]))

pylab.title('Order life in stock-out in hours', fontsize=20)
pylab.boxplot(stock_out_data)
#pylab.xticks([(i + 1) for i in range(len(stock_out_data.values()))], \
 #            ['%s' % i for i in stock_out_data.keys()])
pylab.show()
