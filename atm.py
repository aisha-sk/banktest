
import mysql.connector as sql

from datetime import date

todaydate = str(date.today())

conn=sql.connect(host='localhost',user='root',password='aisha585',database='BANK')
c1=conn.cursor()
print("================================================================================")

print("BANK MANAGEMENT SYSTEM")

print("================================================================================")
while True:
    print('\nWelcome, thank you for visiting us today.\nTo continue, choose an option from the following.')
    print("1.Signup")
    print("2.Login")
    print("3.Exit")
    print("================================================================================")

    op=int(input("Enter your choice (1/2/3) :"))
    print("================================================================================")

    if op==1:
        c="y"
        while c=="y":
                m=int(input("Enter a 4 digit number as account number:"))
                cb="select * from records where ACCOUNTNUM={}".format(m)
                c1.execute(cb)
                d=c1.fetchall()
                data=c1.rowcount
                if data==1:
                    print("================================================================================")

                    print("This account number already exists:")
                    c=input("Do you want to continue y/n -")
                    print("================================================================================")

                    if c=="y":
                            continue
                    else:
                            print("Thank you.")
                            
                            print("================================================================================")
                    

                else:
                    name=input("Enter name:")
                    passw=int(input("Enter password:"))
                    ab="insert into records(ACCOUNTNUM,PASSWORD,NAME) values({},{},'{}')".format(m,passw,name)
                    print("================================================================================")

                    c1.execute(ab)
                    conn.commit()
                    print("Account has been sucessfully created!")
                    print("The minimum balance in an account is alloted to be 1000 ")
                    print("================================================================================") 

                    s=int(input("Enter the amount to be deposited : "))
                    print("================================================================================")

                    sr="update records set  CREATEAMT={} where ACCOUNTNUM={}".format(s,m)
                    c1.execute(sr)
                    conn.commit()
                    ef="update records set balance=CREATEAMT-withdrawl where ACCOUNTNUM={}".format(m)
                    c1.execute(ef)
                    conn.commit()
                    print("sucessfully deposited")

                    print("Thank you")
                    print("Visit again")
                    break
    if op==2:
        y="y"
        while y=="y":
                
                acct=int(input("Enter account number:"))
                
                cb="select * from records where ACCOUNTNUM={}".format(acct)
                c1.execute(cb)
                c1.fetchall()
                data=c1.rowcount
                if data==1:
                    pas=int(input("Enter password  :"))
                    print("================================================================================")

                    e="select password from records where ACCOUNTNUM={}".format(acct)
                    c1.execute(e)
                    a=c1.fetchone()
                    d=list(a)
                    if pas==d[0]:
                        
                            print("1.Depositing money")
                            print("2.Withdrawing money")
                            print("3.Transfering money")
                            print("4.Checking balance")
                            print("5.Changing Account number ")
                            print("6.View Transaction History")
                            print("7.Closing bank account") #REMOVE
                            print("8.Take Loan")
                            print("0.Exit")
                            print("================================================================================")

                            r=int(input("Enter your choice:"))
                            print("================================================================================")

                            if r==1:
                                amt=int(input("Enter the money to be deposited:"))
                                print("================================================================================")

                                sr="update records set CREATEAMT=CREATEAMT+ {} where ACCOUNTNUM={}".format(amt,acct)
                                c1.execute(sr)
                                conn.commit()
                                ef="update records set balance=CREATEAMT-withdrawl where ACCOUNTNUM={}".format(acct)
                                c1.execute(ef)
                                conn.commit()
                                print("sucessfully deposited")
                                
                                cz="insert into TRANSACTIONHISTORY(accountnum,moneytransac) values({},{})".format(acct,amt)
                                c1.execute(cz)
                                conn.commit()
                                cz2="update TRANSACTIONHISTORY set dates='%s' where accountnum=%d"%(todaydate,acct)
                                c1.execute(cz2)
                                conn.commit()
                                
                                t=input("Do you want to continue y/n -")
                                print("================================================================================")

                                if t=="y":
                                        continue
                                else:
                                        print("Thank you")
                                        break

                            if r==2:
                                amt=int(input("Enter the money to withdraw:"))
                                print("================================================================================")

                                ah="select  BALANCE from records where ACCOUNTNUM={}".format(acct)
                                c1.execute(ah)
                                m=c1.fetchone()
                                if amt >m[0]:
                                        print("Your are having less than",amt)
                                        print("Please try again")
                                        print("================================================================================")

                                else:
                                        sr="update records set balance=balance - {}  where ACCOUNTNUM={}".format(amt,acct)
                                        ed="update records set  WITHDRAWL ={}  where ACCOUNTNUM={}".format(amt,acct)
                                        c1.execute(ed)
                                        c1.execute(sr)
                                        conn.commit()
                                        print("Sucessfully updatad")
                                y=input("do you want to continue y/n -")
                                if y=="y":
                                        continue
                                else:
                                        print("Thank you")
                                        break
                            
                            if r==3:
                                act=int(input("Enter the account number where amount is to be deposited:"))

                                print("================================================================================")

                                cb="select * from records where ACCOUNTNUM={}".format(act)
                                c1.execute(cb)
                                c1.fetchall()
                                data=c1.rowcount
                                if data==1:
                                        print(act ,"number exists")
                                        m=int(input("Enter the money to be transferred :"))

                                        print("================================================================================")

                                        ah="select  BALANCE from records where ACCOUNTNUM={}".format(acct)
                                        c1.execute(ah)
                                        c=c1.fetchone()
                                        if m > c[0]:
                                            print("Your account has less than ",m)
                                            print("Please try again.")

                                            print("================================================================================")

                                        else:
                                            av="update records set balance=balance-{} where ACCOUNTNUM={}".format(m,acct)  
                                            cv="update records set balance=balance+{} where ACCOUNTNUM={}".format(m,act)
                                            w="update records set withdrawl=withdrawl+{} where ACCOUNTNUM={}".format(m,acct)
                                            t="update records set  CREATEAMT=CREATEAMT+{} where ACCOUNTNUM={}".format(m,act)
                                            c1.execute(av)
                                            c1.execute(cv)
                                            c1.execute(w)
                                            c1.execute(t)
                                            conn.commit()
                                            print("Sucessfully transfered")
                                        y=input("Do you want to continue? (y/n) -")
                                        if y=="y":
                                            continue
                                        else:
                                            print("Thank you")
                                            break
                            if r==4:
                                ma="select balance from records where ACCOUNTNUM={}".format(acct)
                                c1.execute(ma)
                                k=c1.fetchone()
                                print("Balance in your account=",k)
                                print("================================================================================")

                                y=input("Do you want to continue? (y/n) -")
                                if y=="y":
                                        continue
                                else:
                                        print("Thank you")
                                        break
                            if r==5:
                                i=int(input("Enter your new account number:"))
                                cb="select * from records where ACCOUNTNUM={}".format(i)
                                c1.execute(cb)
                                c1.fetchall()
                                data=c1.rowcount
                                if data==1:
                                        print("This number already exists")
                                        print("Try again")

                                        y=input("Do you want to continue? (y/n) -")
                                        if y=="y":
                                            continue
                                        else:
                                            print("Thank you")
                                            break
                                else:
                                        name=input("Enter your name")
                                        ar="Update records set ACCOUNTNUM={} where name='{}' and password={}".format(i,name,pas)
                                        c1.execute(ar)
                                        conn.commit()
                                        print("Your new account number is ",i)

                            if r==6:
                                acct=eval(input('Enter your account number: '))
                                c1.execute("select * from transactionhistory where accountnum=%d"%(acct))
                                for i in c1:
                                        print('Account Number: ',i[0], '  Money Deposited: ',i[1], '  Date: ',i[2])



                            if r==7:
                                name=input('Enter account holder\'s name for verification: ')
                                cl="delete from records where ACCOUNTNUM={}".format(acct)
                                c1.execute(cl)
                                conn.commit()
                                print("Account successfully closed.")
                                
                                t=input("Do you want to continue ? (y/n) -")
                                print("================================================================================")

                                if t=="y":
                                        continue
                                else:
                                        print("Thank you")
                                        break

                            if r==8:
                                acct1=int(input('Enter your account number: '))
                                loantype=str(input('Enter loan type:'))
                                amt1=int(input('Enter loan amount:'))
                                col1=str(input('Enter collateral:'))
                                c1.execute("insert into loans values(%d,'%s',%d,'%s','2023-8-1','%s')"%(acct1,loantype,amt1,todaydate,col1))
                                conn.commit()

                                print('\nYour loan expiry date is 2023-8-1\n')

                                

                            if r==0:
                                break
                
                    
                    else:
                            print("Wrong password")
                            print("================================================================================")

                            y=input("do you want to continue ? (y/n)-")
                            if t=="y":
                                        continue
                            else:
                                    print("Thank you")
                                    break
                
                    
                else:
                    print("Your account does not exist.")
                    break

        

    if op==3:
        print("Exiting...")
        break
