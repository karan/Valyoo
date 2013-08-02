import csv
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data = csv.reader(open('cumulative_data.csv', 'r'))
    next(data, None) # skip the headers

    result = {}
    for row in data:
        prod_type = row[1]
        if prod_type in result:
            result[prod_type] += 1
        else:
            result[prod_type] = 1

    total_orders = sum(result.values()) # this is why i <3 python

    print "Total orders %d" % total_orders

    total_sum = 0.00
    for key in result:
        result[key] = result[key] * 100 / total_orders
        total_sum += result[key]

    print result

    plt.bar(range(len(result)), result.values(), 0.50, align='center')
    plt.xticks(range(len(result)), result.keys())
    plt.show()
