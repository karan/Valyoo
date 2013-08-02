import MySQLdb
import datetime

if __name__ == '__main__':

    # datetime.datetime indices:
    # 5
    # 6
    # 7
    # 10
    # 11
    # 14

    rows = [
        (u'Lenskart', u'1200667194', u'Prescription Card', u'41420', u'shipping_accessories', datetime.datetime(2013, 7, 27, 4, 12, 56), datetime.datetime(2013, 7, 27, 11, 18, 4), datetime.datetime(2013, 7, 27, 11, 45, 32), u'0', None, datetime.datetime(2013, 7, 28, 3, 24, 17), u'0000-00-00 00:00:00', u'complete', None, datetime.datetime(2013, 7, 27, 9, 42, 56), 0, None, None, 0, None, None, 0),
        (u'Lenskart', u'1200667195', u'Rs.1800 Coupon Booklet ( Rs. 500 Coupons)  - FREE', u'39799', u'shipping_accessories', datetime.datetime(2013, 7, 27, 4, 13, 17), datetime.datetime(2013, 7, 27, 10, 10, 2), datetime.datetime(2013, 7, 27, 10, 53, 32), u'1', None, datetime.datetime(2013, 7, 27, 12, 12, 2), u'0000-00-00 00:00:00', u'complete', u'complete', datetime.datetime(2013, 7, 27, 9, 43, 17), 0, None, None, 0, None, None, 0),
        (u'Lenskart', u'1200667196', u'Vincent Chase RG 172 Gunmetal C3 Eyeglasses', u'58131', u'eyeframe', datetime.datetime(2013, 7, 27, 4, 13, 31), datetime.datetime(2013, 7, 27, 10, 10, 2), datetime.datetime(2013, 7, 27, 12, 54, 34), u'1', None, datetime.datetime(2013, 7, 28, 4, 49, 13), u'0000-00-00 00:00:00', u'complete', None, datetime.datetime(2013, 7, 27, 9, 43, 31), 0, None, None, 0, None, None, 0),
        (u'Lenskart', u'1200667193', u'Prescription Card', u'41420', u'shipping_accessories', datetime.datetime(2013, 7, 27, 4, 11, 10), datetime.datetime(2013, 7, 27, 10, 12, 4), datetime.datetime(2013, 7, 27, 11, 37, 47), u'0', None, datetime.datetime(2013, 7, 27, 19, 51, 13), u'2013-07-29 00:00:00', u'delivered', None, datetime.datetime(2013, 7, 27, 9, 41, 10), 0, None, None, 0, None, None, 0),
        (u'Lenskart', u'1200667193', u'Prescription-Lens PC SV Regular', u'45081', u'prescription_lens', datetime.datetime(2013, 7, 27, 4, 11, 10), datetime.datetime(2013, 7, 27, 10, 12, 4), datetime.datetime(2013, 7, 27, 17, 51, 33), u'0', None, datetime.datetime(2013, 7, 27, 19, 51, 13), u'2013-07-29 00:00:00', u'delivered', None, datetime.datetime(2013, 7, 27, 9, 41, 10), 0, None, None, 0, None, None, 0),
        (u'Lenskart', u'1200667190', u'Rs.1800 Coupon Booklet ( Rs. 500 Coupons)  - FREE', u'39799', u'shipping_accessories', datetime.datetime(2013, 7, 27, 4, 10, 33), datetime.datetime(2013, 7, 27, 10, 7, 4), datetime.datetime(2013, 7, 27, 10, 56, 2), u'1', None, datetime.datetime(2013, 7, 27, 14, 33, 21), u'0000-00-00 00:00:00', u'complete', u'complete', datetime.datetime(2013, 7, 27, 9, 40, 33), 0, None, None, 0, None, None, 0),
        (u'Lenskart', u'1200667187', u'Prescription-Lens CR SV Regular', u'45073', u'prescription_lens', datetime.datetime(2013, 7, 27, 4, 8, 48), datetime.datetime(2013, 7, 27, 9, 58, 2), datetime.datetime(2013, 7, 27, 12, 11, 25), u'0', None, datetime.datetime(2013, 7, 27, 17, 0, 1), u'2013-07-30 00:00:00', u'delivered', None, datetime.datetime(2013, 7, 27, 9, 38, 48), 0, None, None, 0, None, None, 0),
        (u'Lenskart', u'1200667183', u'Rs.1800 Coupon Booklet ( Rs. 500 Coupons)  - FREE', u'39799', u'shipping_accessories', datetime.datetime(2013, 7, 27, 4, 3, 46), datetime.datetime(2013, 7, 27, 11, 44, 3), datetime.datetime(2013, 7, 27, 12, 26, 48), u'1', None, datetime.datetime(2013, 7, 27, 17, 46, 17), u'2013-07-30 00:00:00', u'delivered', None, datetime.datetime(2013, 7, 27, 9, 33, 46), 0, None, None, 0, None, None, 0),
        (u'Lenskart', u'1200667183', u'Prescription-Lens CR SV Regular', u'45073', u'prescription_lens', datetime.datetime(2013, 7, 27, 4, 3, 46), datetime.datetime(2013, 7, 27, 11, 44, 3), datetime.datetime(2013, 7, 27, 13, 50, 35), u'0', None, datetime.datetime(2013, 7, 27, 17, 46, 17), u'2013-07-30 00:00:00', u'delivered', None, datetime.datetime(2013, 7, 27, 9, 33, 46), 0, None, None, 0, None, None, 0),
        (u'Lenskart', u'1200667175', u'Bausch & Lomb Soflens 59 (6 Lenses/box)_S:-4.75 / C:0.00 / A:0 / BC:8.60 / AP:0.00 / CL:', u'90000443', u'contact_lens', datetime.datetime(2013, 7, 27, 3, 58, 6), datetime.datetime(2013, 7, 27, 9, 38, 2), datetime.datetime(2013, 7, 27, 10, 10, 22), u'0', None, datetime.datetime(2013, 7, 27, 12, 32, 17), u'2013-07-29 00:00:00', u'delivered', u'complete', datetime.datetime(2013, 7, 27, 9, 28, 6), 0, None, None, 0, None, None, 0),
        (u'Lenskart', u'1200667171', u'Rs.1800 Coupon Booklet ( Rs. 500 Coupons)  - FREE', u'39799', u'shipping_accessories', datetime.datetime(2013, 7, 27, 3, 55, 56), datetime.datetime(2013, 7, 27, 9, 37, 3), datetime.datetime(2013, 7, 27, 9, 51, 47), u'1', None, datetime.datetime(2013, 7, 27, 12, 59, 50), u'0000-00-00 00:00:00', u'complete', u'complete', datetime.datetime(2013, 7, 27, 9, 25, 56), 0, None, None, 0, None, None, 0),
        (u'Lenskart', u'1200667165', u'Rs.1800 Coupon Booklet ( Rs. 500 Coupons)  - FREE', u'39799', u'shipping_accessories', datetime.datetime(2013, 7, 27, 9, 20), datetime.datetime(2013, 7, 27, 9, 30, 4), datetime.datetime(2013, 7, 27, 10, 24, 35), u'1', None, datetime.datetime(2013, 7, 27, 16, 15, 14), u'2013-07-29 00:00:00', u'delivered', u'complete', datetime.datetime(2013, 7, 27, 14, 50), 0, None, None, 0, None, None, 0),
        (u'Bagskart', u'1200667151', u'Feelgood Backpack FG011-A Navy Blue', u'35607', u'Backpacks', datetime.datetime(2013, 7, 27, 2, 14, 52), u'', datetime.datetime(2013, 7, 27, 12, 50, 15), u'1', None, datetime.datetime(2013, 7, 27, 15, 16, 32), u'2013-07-29 00:00:00', u'delivered', u'complete', datetime.datetime(2013, 7, 27, 7, 44, 52), 0, None, None, 0, None, None, 0),
        (u'Lenskart', u'1200667148', u'Rs.1800 Coupon Booklet ( Rs. 500 Coupons)  - FREE', u'39799', u'shipping_accessories', datetime.datetime(2013, 7, 27, 2, 8, 40), datetime.datetime(2013, 7, 27, 7, 41, 3), datetime.datetime(2013, 7, 27, 7, 50, 37), u'1', None, datetime.datetime(2013, 7, 27, 12, 9, 49), u'2013-07-29 00:00:00', u'complete', u'complete', datetime.datetime(2013, 7, 27, 7, 38, 40), 0, None, None, 0, None, None, 0)
        ]
    db = MySQLdb.connect(host="localhost", # your host, usually localhost
                         #port=5123, # port of the connection
                         user="root", # your username
                          passwd="", # your password
                          db="inventory") # name of the data base

    # you must create a Cursor object. It will let
    #  you execute all the query you need
    cur = db.cursor()

    sql = """INSERT INTO daily_dispatch VALUES ({})""".format(', '.join(['%s']*22))

    row = rows[0]
    
    cur.executemany(sql, rows)
    
    db.commit()
    
    # Use all the SQL you like
    cur.execute("""select * from daily_dispatch""")

    print cur.fetchall()
    
    db.close()
