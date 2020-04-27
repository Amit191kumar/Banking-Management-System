from pymysql import *
def openconnection():
    con=connect(db='bank',user='root',passwd='root',host='localhost')
    return con
def openaccount(acno,name,dateofopen,amt):
    con=openconnection()
    cur=con.cursor()
    cur.execute("select * from accountdetails where acno=%d"%(acno))
    rs=cur.fetchall()
    if len(rs)>0:
        print('Duplicate Account')
    else:
        i=cur.execute("insert into accountdetails values(%d,'%s','%s',%f)"%(acno,name,dateofopen,amt))
        if i==1:
            con.commit()
            print('account created')
            con.close()
def deposit(acno,amt,dod):
    ttype='D'
    con=openconnection()
    cur=con.cursor()
    i=cur.execute("update accountdetails set balance=balance+%f where acno=%d"%(amt,acno))
    if i==1:
        j=cur.execute("insert into transdetail values(%d,'%s',%f,'%s')"%(acno,dod,amt,ttype))
        if j==1:
            con.commit()
            print('Amount Deposite')
            con.close()
        else:
            print('Not account Holder ')
    else:
        print('No Account In Bank')
def withdrawl(acno,amt,dod):
    ttype='W'
    con=openconnection()
    cur=con.cursor()
    cur.execute("select balance from accountdetails where acno=%d"%(acno))
    rs=cur.fetchall()
    if len(rs)>0:
        bal=rs[0][0]
        if amt<bal:
            abal=bal-amt
            if abal>1000:

            	
            	i=cur.execute("update accountdetails set balance=balance-%f where acno=%d"%(amt,acno))
            	if i==1:
            		j=cur.execute("insert into transdetail values(%d,'%s',%f,'%s')"%(acno,dod,amt,ttype))
            		if j==1:
            			con.commit()
            			print('Amount Withdrawn')
            			con.close()
            		else:
            			print('Not account Holder ')
            	else:
            		print('No Account In Bank')
            else:
                print('Must maintain minimum account balance')
        else:
        	print('Low Balance')
    else:
    	print(" Account Not In Bank")

def balance(acno):
    con=openconnection()
    cur=con.cursor()
    cur.callproc('bankshow',[acno])
    #cur.execute("select balance from accountdetails where acno=%d"%(acno))
    rs=cur.fetchall()
    if len(rs)>0:
        #print('Account No:- ',acno)
        print('Balance:- ',rs[0][1])
        print('Name :- ',rs[0][0])
    else:
        print('Record Not Found')
        