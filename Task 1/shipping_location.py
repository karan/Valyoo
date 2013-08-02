import csv

ship = csv.reader(open('shipping.csv', 'r'))
next(ship, None)

ship_loc = csv.writer(open('shipping-locations.csv', 'wb'))

ship_loc.writerow(['increment', 'order id', 'carrier', 'hours', 'city', 'zip'])

count = 0
for ship_row in ship:
    orders_data = csv.reader(open('data/orders with id.csv', 'r'))
    increment = ship_row[0]
    carrier = ship_row[1]
    hours = ship_row[2]
    for row in orders_data:
        order_id = row[0]
        inc = row[1]
        city = row[2]
        zip_code = row[3]
        if increment == inc:
            break
    ship_loc.writerow([increment, order_id, carrier, hours, city, zip_code])
    count += 1
    if count % 100 == 0:
        print '%d done' % count
