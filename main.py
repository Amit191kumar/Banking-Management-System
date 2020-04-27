from bankutil import *
from pymysql import *
ans='y'
while ans=='y':
    print('1. Open account')
    print('2. Deposite account')
    print('3. Withdrawal amount')
    print('4. show Balance')
    print('5 Exit')
    print('Enter choice 1....5')
    choice= int(input())
    if choice==1:
        acno=int(input('Account No :- '))
        name=input('Name of Person:-  ')
        doo=input('Enter Date yyyy-mm-dd :- ')
        amt=float(input('Enter amount :- '))
        openaccount(acno,name,doo,amt)
    elif choice==2:
        acno=int(input('Account No :- '))
        dod=input('Enter Date yyyy-mm-dd :- ')
        amt=float(input('Enter amount :- '))
        deposit(acno,amt,dod)
    elif choice==3:
        acno=int(input('Account No :- '))
        dod=input('Enter Date yyyy-mm-dd :- ')
        amt=float(input('Enter amount :- '))
        withdrawl(acno,amt,dod)
    elif choice==4:
        acno=int(input('Account No :- '))
        balance(acno)
    elif choice==5:
        exit(0)
    print('continue...y/n')
    ans=input()