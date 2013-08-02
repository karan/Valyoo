#!/usr/bin/python

# author: Karan Goel

######### IMPORTS #########
from bs4 import BeautifulSoup # pip install beautifulsoup
import urllib2
import MySQLdb
from datetime import datetime
from datetime import timedelta
######### IMPORTS #########


######### METHODS #########

def convert_to_datetime(date):
    """
    Parameter:
    date - string (YYYY-MM-DD HH:mm:ss)
    Converts passed string date to datetime.datetime object.
    """
    try:
        fmt = '%Y-%m-%d %H:%M:%S'
        return datetime.strptime(str(date), fmt)
    except:
        return date

def get_actual_order_date(order_date):
    """
    Parameter:
    order_date - string (YYYY-MM-DD HH:mm:ss)
    Converts GMT time to IST by adding 5:30 to passed time.
    """
    order = convert_to_datetime(order_date)
    change = timedelta(hours=5, minutes=30)
    return order + change

def is_todays_order(date):
    """
    Returns 1 if passed date is today's and hour is less
    than 16, 0 otherwise.
    """
    return 1 if (datetime.now().date() == date.date() and date.time().hour < 16) else 0

def is_yesterdays(date):
    """
    Returns 1 if passed date is yesterday's and hour is less
    than 16, 0 otherwise.
    """
    change = timedelta(days=1)
    if (datetime.now().date() - change == date.date() and date.time().hour < 16):
        return 1
    return 0

def is_same_day(date1, date2, what):
    """
    Parameters:
    date1 = datetime.datetime object (YYYY-MM-DD HH:mm:ss)
    date2 = datetime.datetime object (YYYY-MM-DD HH:mm:ss)
    Returns:
    Only for same dates:
        d (dipatch) - 1 if hour of date2 < 20, 0 otherwise
        so (stockout) - 1 if hour of date2 < 17, 0 otherwise
    """
    try:
        if what == 'd': # dispatch
            return 1 if (date2.time().hour < 20) else 0
        elif what == 'so': # stockout
            return 1 if (date2.time().hour < 17) else 0
    except:
        return 0
######### METHODS #########


######### MAIN #########
REPORTS_URL = 'http://192.168.1.140/reports/fat_old.php'

if __name__ == '__main__':
    print "Connecting to %s..." % REPORTS_URL
    url = urllib2.urlopen(REPORTS_URL)
    content = url.read()

    print "Page read...\nLoading content into corpora.."
    soup = BeautifulSoup(content)
    table = soup.findChildren('table')[0] # 0 because only table on page

    print "Finding data rows..."
    rows = table.findChildren(['tr'])[1:] # gets all rows, removes the header row
    print '%d data rows found..' % len(rows)
    
    rows_data = [] # will hold all rows as list of tuples

    print "Parsing data rows..."

    for row in rows:
        single_row_content = [] # list to hold one complete row
        cells = row.findChildren('td') # will get all data cells within single row
        for cell in cells:
            single_row_content.append(cell.string)
        for i in range(len(single_row_content)):
            # remove all unneeded characters (\r, \n, \t)
            try:
                single_row_content[i] = single_row_content[i].replace('\r', '')
                single_row_content[i] = single_row_content[i].replace('\n', '')
                single_row_content[i] = single_row_content[i].replace('\t', '')
            except:
                pass

        ### Fill all other cells ###
        #-- Convert all date strings to datetime objects --#
        single_row_content[5] = convert_to_datetime(single_row_content[5])
        single_row_content[6] = convert_to_datetime(single_row_content[6])
        single_row_content[7] = convert_to_datetime(single_row_content[7])
        single_row_content[10] = convert_to_datetime(single_row_content[10])
        #-- Convert all date strings to datetime objects --#

        #-- Temp variable assignments --#
        order_date = single_row_content[5]
        stock_out = single_row_content[7]
        power_complete = single_row_content[6]
        ship = single_row_content[10]
        #-- Temp variable assignments --#

        actual_order_date = get_actual_order_date(order_date) # single_row_content[14]

        same_day_dispatch, same_day_stockout = None, None
        todays_order = is_todays_order(actual_order_date) # single_row_content[15]
        if todays_order: # todays_order == 1
            # single_row_content[16]
            same_day_dispatch = is_same_day(actual_order_date, ship, 'd')
            # single_row_content[17]
            same_day_stockout = is_same_day(actual_order_date, stock_out, 'so')

        yesterdays_dispatch, yesterdays_stockout = None, None
        yesterdays_order = is_yesterdays(actual_order_date) # single_row_content[18]
        if yesterdays_order: # yesterdays_order = 1
            # single_row_content[19]
            yesterdays_dispatch = is_same_day(actual_order_date, ship, 'd')
            # single_row_content[20]
            yesterdays_stockout = is_same_day(actual_order_date, stock_out, 'so')
        eyeframe_less_than_one = yesterdays_order # single_row_content[21]
        ### Fill all other cells ###

        # add everything found to our row
        single_row_content.extend([actual_order_date, todays_order, same_day_dispatch, \
                                   same_day_stockout, yesterdays_order, yesterdays_dispatch, \
                                   yesterdays_stockout, eyeframe_less_than_one])

        # change the list to a tuple
        single_row_content = tuple(single_row_content)
        # add the single row to out list of rows
        rows_data.append(single_row_content)


    print 'All data parsed, preparing to write to DB...'

    db = MySQLdb.connect(host="192.168.1.22", # your host
                         port=, # port of the connection
                         user="", # your username
                          passwd="", # your password
                          db="") # name of the data base

    print 'Connection to database established...'
    # you must create a Cursor object. It will let
    #  you execute all the query you need
    cur = db.cursor()

    # Empty the table to prepare writing of new data
    print 'Deleting existing data..'
    sql = "TRUNCATE TABLE daily_dispatch;"
    cur.execute(sql)
    db.commit()

    # Use all the SQL you like
    sql = """INSERT INTO daily_dispatch VALUES ({})""".format(', '.join(['%s']*22))

    # Execute the query, insert all tuples
    print 'Executing query to write new data...'
    cur.executemany(sql, rows_data)
    
    # commit the changes, or db rolls back
    print 'Committing changes to database...'
    db.commit()

    # close the connection
    print 'Connection to DB closed'
    db.close()
    
######### MAIN #########
