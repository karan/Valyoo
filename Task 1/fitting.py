import csv
from datetime import datetime

data = csv.reader(open('cumulative_data.csv', 'r'))
next(data, None) # skip the headers

ship_data = csv.writer(open('fitting.csv', 'wb'))
ship_data.writerow(['order', 'hours'])

for row in data:
    if row[3] != '' and row[4] != '':
        t1 = row[4]
        t2 = row[3]
        FMT = '%Y-%m-%d %H:%M:%S'
        #FMT = '%m/%d/%Y %H:%M'
        tdelta = datetime.strptime(t1, FMT) - datetime.strptime(t2, FMT)
        hours = tdelta.total_seconds() / 60 / 60
        print row[0], t1, t2, hours
        if hours > 0.00:
            ship_data.writerow([row[0], hours]) # save as hours
