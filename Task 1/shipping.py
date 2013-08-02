import csv
from datetime import datetime

data = csv.reader(open('cumulative_data.csv', 'r'))
next(data, None) # skip the headers

ship_data = csv.writer(open('shipping.csv', 'wb'))
ship_data.writerow(['prder', 'carrier', 'ship time'])

for row in data:
    if row[6] != '' and row[7] != '' and row[8] != '':
        t1 = row[7]
        t2 = row[6]
        FMT = '%Y-%m-%d %H:%M:%S'
        tdelta = datetime.strptime(t1, FMT) - datetime.strptime(t2, FMT)
        hours = tdelta.total_seconds() / 60 / 60
        print row[0], t1, t2, hours
        if hours > 0.00:
            ship_data.writerow([row[0], row[8], hours]) # save as hours
