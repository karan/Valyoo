import csv

def get_classification(product_id):
    prod = csv.reader(open('data/products.csv')) # product id, class id
    next(prod, None) # skip the headers

    classification = csv.reader(open('data/classification.csv')) # class id, type
    next(classification, None) # skip the headers

    for row in prod:
        if row[0] == product_id:
            class_id = row[1]
            for class_row in classification:
                if class_row[0] == class_id:
                    return class_row[1]


def find_stock_out(order_id):
    stock_out = csv.reader(open('data/stock_out.csv')) # order no, product id, date, barcode
    next(stock_out, None) # skip the headers
    for row in stock_out:
        if row[0] == order_id:
            return row[2]


def find_fitting(order_id):
    fitting = csv.reader(open('data/fitting_complete.csv')) # order no, product id, date
    next(fitting, None) # skip the headers
    for row in fitting:
        if row[0] == order_id:
            return row[2]
        

def find_qc(order_id):
    qc = csv.reader(open('data/qccheck.csv')) # order no, product id, date
    next(qc, None) # skip the headers
    for row in qc:
        if row[0] == order_id:
            return row[2]


def find_ship(order_id):
    ship = csv.reader(open('data/shipping_status.csv')) # order no, start time, carrier, end time
    next(ship, None) # skip the headers
    for row in ship:
        if row[0] == order_id:
            return [row[1], row[3], row[2]]



if __name__ == '__main__':
    orders = csv.reader(open('data/orders.csv')) # order no, product id, date
    next(orders, None) # skip the headers

    all_data = csv.writer(open('data/cumulative_data.csv', 'wb'))
    all_data.writerow(['order_id', 'type', 'created', 'stock_out', 'fitting', \
                       'qc_check', 'ship_start', 'ship_end', 'carrier'])
    count = 0
    for single_order in orders:
        count += 1
        order_id = single_order[0]
        classify = get_classification(single_order[1]) # single_order[1] is product ID
        created = single_order[2]
        stock_out = find_stock_out(order_id)
        fitting = find_fitting(order_id)
        qc_check = find_qc(order_id)
        ship = find_ship(order_id)
        if ship is not None and ship[1] is not None:
            all_data.writerow([order_id, classify, created, stock_out, \
                               fitting, qc_check, ship[0], ship[1], ship[2]])
        else:
            all_data.writerow([order_id, classify, created, stock_out, \
                               fitting, qc_check, "", "", ""])
        if count % 50 == 0:
            print "%d done!" % count
    all_data.close()
