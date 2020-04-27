from pymysql import *
con=connect(db='bank',user='root',passwd='root',host='localhost')
cur=con.cursor()
acno=(int)(input('Account No'))
cur.callproc('bankshow',[acno])
rs=cur.fetchall()
print(rs)