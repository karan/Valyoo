import csv
from datetime import datetime

data = csv.reader(open('cumulative_data.csv', 'r'))
next(data, None) # skip the headers

qc_data = csv.writer(open('qc.csv', 'wb'))
qc_data.writerow(['order', 'hours'])

for row in data:
    if row[4] != '' and row[5] != '':
        t1 = row[5]
        t2 = row[4]
        FMT = '%Y-%m-%d %H:%M:%S'
        #FMT = '%m/%d/%Y %H:%M'
        tdelta = datetime.strptime(t1, FMT) - datetime.strptime(t2, FMT)
        hours = tdelta.total_seconds() / 60 / 60
        print row[0], t1, t2, hours
        if hours > 0.00:
            qc_data.writerow([row[0], hours]) # save as hours
