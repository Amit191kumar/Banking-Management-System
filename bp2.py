from pymysql import *
con=connect(db='bank',user='root',passwd='root',host='localhost')
cur=con.cursor()
cur.callproc('show_record')
rs=cur.fetchall()
print(rs)