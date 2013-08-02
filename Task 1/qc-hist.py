import csv
import matplotlib.pyplot as plt

data = csv.reader(open('qc.csv', 'r'))
next(data, None) # skip the headers 

qc_data = []

for row in data:
    qc_data.append(float(row[1]))

plt.hist(qc_data, bins=20, color='r', label='Fitting life')
plt.title('Order life in QC in hours')
plt.xlabel('Hours')
plt.ylabel('Quantity')
plt.show()
