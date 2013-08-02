import csv
import matplotlib.pyplot as plt

data = csv.reader(open('stock-out.csv', 'r'))
next(data, None) # skip the headers 

stock_out_data = []

for row in data:
    stock_out_data.append(float(row[1]))

plt.hist(stock_out_data, bins=20, color='r', label='Stock-Out life')
plt.title('Order life in stock-out in hours')
plt.xlabel('Hours')
plt.ylabel('Quantity')
plt.show()
