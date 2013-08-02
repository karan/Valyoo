import csv
import matplotlib.pyplot as plt

data = csv.reader(open('fitting.csv', 'r'))
next(data, None) # skip the headers 

fitting_data = []

for row in data:
    fitting_data.append(float(row[1]))

plt.hist(fitting_data, bins=20, color='r', label='Stock-Out life')
plt.title('Order life in fitting in hours')
plt.xlabel('Hours')
plt.ylabel('Quantity')
plt.show()
