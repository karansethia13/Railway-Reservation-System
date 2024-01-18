# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 18:01:08 2022

@author: Om
"""
from tkinter import *
import random
def menu():
    print('1.YES')
    print('2.NO')
    ch=int(input('DO YOU WANT TO CONTINUE OR NOT:'))
    while ch==1:
        print('WELECOME TO ONLINE RAILWAY RESERVATION SYSTEM') 
        print('1.SIGN IN')
        print('2.SIGN UP')
        print('3.DELETE ACCOUNT')
        print('4.EXIT')
        ch1=int(input('ENTER YOUR CHOICE:'))
        if ch1==1:
            a=checking()
            if a==True:
                print('WELCOME')
                main()
            else:
                
                continue
        elif ch1==2:
            a=checking_1()
            if a==True:
                main()
            else:
                print('PASSWORD ALREADY EXISTS')
                continue
            
            
        elif ch1==3:
            c=checking_2()
            if c==True:
               
                print('ACCOUNT DELETED')
                continue
            else:
                print('YOUR PASSWAORD OR USER_NAME IS INCORRECT')
                continue
        elif ch1==4:
            print('THANK YOU')
            break
        else:
            print('ERROR 404:PAGE NOT FOUND')
            break
def main():        
    print('1.yes')
    print('2.no')
    c=int(input("do you want to continue or not:"))
    while (c==1):
        print(' 1.TICKET BOOKING',"\n", '2.TICKET CHECKING',"\n",'3.TICKET CANCELLING',"\n",'4.ACCOUNT DETAILS',"\n",'5.LOG OUT')
        ch=int(input('enter ur choice:'))
        if ch==1:
            ticket_booking()
        elif ch==2:
            ticket_checking()
        elif ch==3:
            ticket_cancelling()
        elif ch==4:
            checking_3()
            
                
        elif ch==5:
            print('THANK YOU')
            break
        else:
            print('WRONG INPUT')
    else:
        print('ERROR 404: ERROR PAGE NOT FOUND')
def ticket_booking():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='12345',database='railway')
    cursor=mycon.cursor()
    mycon.autocommit=True
   
    print()
    
    nm=input('enter your name:')
    phno=input('enter your phone number:')
    age=int(input('enter your age:'))
    print(' M=MALE','\n','F=FEMALE','\n','N=NOT TO MENTION')
    gender=input('enter your gender:')
    Gender=gender.upper()
    print()
    print("Please enter the number corresponding to the city names:")
    print("1.DELHI")
    print("2.MUMBAI")
    print("3.KOLKATA")
    print("4.CHENNAI")
    print("5.BANGALORE")
    print("6.SURAT")
    fr=int(input('enter ur starting point:'))
    to=int(input('enter your destination:'))
    
    if fr>6 or fr<=0:
        print("ERROR 403: Please enter the correct starting point")
    if to>6 or to<=0:
        print("ERROR 405: Please enter the correct destination")   
    
    x=fr*10+to
    date1=input('enter date(dd):')
    date2=input('enter month(mm):')
    date3=input('enter year(yyyy):')
    date=date1+"/"+date2+"/"+date3
    a={'M':'MALE','F':'FEMALE','N':'NOT TO MENTION'}
    v=a[Gender]
    s1="insert into railway values('{}',{},{},'{}','{}','{}','{}')".format(nm,phno,age,v,fr,to,date)
    cursor.execute(s1)
    print('BOOKED SUCCESSFULLY')

    c_no = random.randint(1,5)
    
    
    mycon=mysql.connector.connect(host="localhost", user="root",passwd="12345",database="train")
    cr=mycon.cursor()
    

    if x==12:
        cr.execute("select * from train_info where sl_no=12")
    elif x==13:
        cr.execute("select * from train_info where sl_no=13")
    elif x==14:
        cr.execute("select * from train_info where sl_no=14")
    elif x==15:
        cr.execute("select * from train_info where sl_no=15")
    elif x==16:
        cr.execute("select * from train_info where sl_no=16")
    elif x==21:
        cr.execute("select * from train_info where sl_no=21")
    elif x==23:
        cr.execute("select * from train_info where sl_no=23")
    elif x==24:
        cr.execute("select * from train_info where sl_no=24")
    elif x==25:
        cr.execute("select * from train_info where sl_no=25")
    elif x==26:
        cr.execute("select * from train_info where sl_no=26")
    elif x==31:
        cr.execute("select * from train_info where sl_no=31")
    elif x==32:
        cr.execute("select * from train_info where sl_no=32")
    elif x==34:
        cr.execute("select * from train_info where sl_no=34")
    elif x==35:
        cr.execute("select * from train_info where sl_no=35")
    elif x==36:
        cr.execute("select * from train_info where sl_no=36")
    elif x==41:
        cr.execute("select * from train_info where sl_no=41")
    elif x==42:
        cr.execute("select * from train_info where sl_no=42")
    elif x==43:
        cr.execute("select * from train_info where sl_no=43")
    elif x==45:
        cr.execute("select * from train_info where sl_no=45")
    elif x==46:
        cr.execute("select * from train_info where sl_no=46")
    elif x==51:
        cr.execute("select * from train_info where sl_no=51")
    elif x==52:
        cr.execute("select * from train_info where sl_no=52")
    elif x==53:
        cr.execute("select * from train_info where sl_no=53")
    elif x==54:
        cr.execute("select * from train_info where sl_no=54")
    elif x==56:
        cr.execute("select * from train_info where sl_no=56")
    elif x==61:
        cr.execute("select * from train_info where sl_no=61")
    elif x==62:
        cr.execute("select * from train_info where sl_no=62")
    elif x==63:
        cr.execute("select * from train_info where sl_no=63")
    elif x==64:
        cr.execute("select * from train_info where sl_no=64")
    elif x==65:
        cr.execute("select * from train_info where sl_no=65")

    data=cr.fetchall()
    #print(data)

    
    def submit():
        root = Tk()
        root.geometry("250x400")
        root.title("Please Confirm Your Details")
        label1 = Label(root,text="Your Name",padx=10,pady=10)
        label1.grid(row=0,column=0)

        label2 = Label(root,text=nm,padx=10,pady=10)
        label2.grid(row=0,column=1)
         
        
        dict_city={1:"Delhi",2:"Mumbai",3:"Kolkata",4:"Chennai",5:"Bangalore",6:"Surat"}

        label3 = Label(root,text="Your Source City",padx=10,pady=10)
        label3.grid(row=1,column=0)

        label4 = Label(root,text=dict_city[fr],padx=10,pady=10)
        label4.grid(row=1,column=1)

        label5 = Label(root,text="Your Destination",padx=10,pady=10)
        label5.grid(row=2,column=0)
        
        label6 = Label(root,text=dict_city[to],padx=10,pady=10)
        label6.grid(row=2,column=1)

        
        label7 = Label(root,text="Your Phone No.",padx=10,pady=10)
        label7.grid(row=3,column=0)
        
        label8 = Label(root,text=phno,padx=10,pady=10)
        label8.grid(row=3,column=1)
        
        label22 = Label(root,text="Your Gender",padx=10,pady=10)
        label22.grid(row=4,column=0)
        
        label23 = Label(root,text=v,padx=10,pady=10)
        label23.grid(row=4,column=1)

       
        label13 = Label(root,text="Train Name",padx=10,pady=10)
        label13.grid(row=5,column=0)

        label14 = Label(root,text=data[0][1],padx=10,pady=10)
        label14.grid(row=5,column=1)


        label20 = Label(root,text="Compartment no.",padx=10,pady=10)
        label20.grid(row=6,column=0)

        label14 = Label(root,text=c_no,padx=10,pady=10)
        label14.grid(row=6,column=1)

        
        label15 = Label(root,text='Ticket Price',padx=10,pady=10)
        label15.grid(row=7,column=0)
        
        
        label16 = Label(root,text=data[0][2],padx=10,pady=10)
        label16.grid(row=7,column=1)
        mybutton = Button(root,text="Save",command=root.quit,padx = 15,pady = 15,bg = "black", fg = "white",width = 15,borderwidth = 3,relief = SUNKEN)
        mybutton.grid(row = 8,column = 0,columnspan =10,rowspan = 10)
        root.mainloop()
    submit()
    
    
def ticket_checking():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='12345',database='railway')
    cursor=mycon.cursor()
    mycon.autocommit=True
    print('1.yes')
    print('2.no')
    ch=int(input("do you want to continue or not:"))

    if ch==1:
        phno=int(input('enter your phnone number:'))
        try:
            s1="select * from railway where phno=phno"
            cursor.execute(s1)
            data=cursor.fetchall()[0]
            Data=list(data)
            a=['NAME','PHONE NUMBER','AGE','GENDER','STARTING POINT','DESTINATION','DATE',]
            print(a[0],'::::',Data[0].upper())
            print(a[1],'::::',Data[1])
            print(a[2],'::::',Data[2])
            print(a[3],'::::',Data[3].upper())
            print(a[4],'::::',Data[4].upper())
            print(a[5],'::::',Data[5].upper())
            print(a[6],'::::',Data[6])
        except:
            print('TICKET DOES NOT EXISTS')
    elif ch==2:
        print('THANK YOU')
    else:
        print('ERROR 404:PAGE NOT FOUND')
    
       

def ticket_cancelling():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='12345',database='railway')
    cursor=mycon.cursor()
    mycon.autocommit=True
    print('1.yes')
    print('2.no')
    ch=int(input("do you want to continue or not:"))
    if ch==1:
        phno=input('enter your phone number:')
        s1="delete from railway where phno=phno"
        cursor.execute(s1)
        print('TICKET CANCELLED')
    elif ch==2:
        print('THANK YOU')
    else:
        print('ERROR 404:PAGE NOT FOUND')
        
def checking_2():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='12345',database='railway')
    cursor=mycon.cursor()
    mycon.autocommit=True
    a=input('USER NAME:')
    b=input('PASS WORD:')
    try:
        s1="select user_name from user_accounts where password='{}'".format(b)
        cursor.execute(s1)
        data=cursor.fetchall()[0]
        data=list(data)
        if data[0]==a:
             print('IS THIS YOUR ACCOUNT')
             s1="select user_name from user_accounts where password='{}'".format(b)
             c1="select fname,lname from user_accounts where password='{}'".format(b)
             cursor.execute(c1)
             data1=cursor.fetchall()[0]
             data1=list(data1)
             data1=data1[0]+' '+data1[1]
             cursor.execute(s1)
             data=cursor.fetchall()[0]
             data=list(data)
             if data[0]==a:
                 x=['FIRST NAME','LAST NAME','PHONE NUMBER','GENDER','DATE OF BIRTH','AGE']
                 s1="select fname,lname,phno,gender,dob,age from user_accounts where password='{}'".format(b)
                 cursor.execute(s1)
                 data=cursor.fetchall()[0]
                 data=list(data)
                 print(x[0],':::',data[0])
                 print(x[1],':::',data[1])
                 print(x[2],':::',data[2])
                 print(x[3],':::',data[3])
                 print(x[4],':::',data[4])
                 print(x[5],':::',data[5])
                 print('1.yes')
                 print('2.no')
                 vi=int(input('enter your choice:'))
                 if vi==1:
                     b1="delete from user_accounts where password = '{}'".format(b)
                     cursor.execute(b1)
                     return True
                 elif vi==2:
                     print('SORRY,RETRY')
                 else:
                     print('ERROR 404:PAGE NOT FOUND')
        else:
            return False
    except:
        print('ACCOUNT DOES NOT EXIST')
        

def checking_1():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='12345',database='railway')
    cursor=mycon.cursor()
    mycon.autocommit=True
    f=input("FIRST NAME:")
    l=input("LAST NAME:")
    n=f+" "+l
    a=input('USER NAME:')
    b=input('PASS WORD:')
    c=input('RE-ENTER YOUR PASS WORD:')
    ph=input("PHONE NUMBER:")
    print(' M=MALE','\n','F=FEMALE','\n','N=NOT TO MENTION')
    gen=input('ENTER YOUR GENDER:')
    print("ENTER YOR DATE OF BIRTH")
    d=input("DD:")
    o=input("MM:")
    p=input("YYYY:")
    dob=d+'/'+o+'/'+p
    age=input('YOUR AGE:')
    v={'m':'MALE','f':'FEMALE','n':'NOT TO MENTION'}
    if b==c:
        try:
            c1="insert into user_accounts values('{}','{}','{}','{}','{}','{}','{}','{}')".format(f,l,a,b,ph,v[gen],dob,age)
            cursor.execute(c1)
            print('WELCOME',f,' ',l)
            return True
        except:
            print('PASSWORD ALREADY EXISTS')
            return False
    else:
        print('BOTH PASSWORDS ARE NOT MATCHING')
        


def checking():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='12345',database='railway')
    cursor=mycon.cursor()
    mycon.autocommit=True
    a=input('USER NAME:')
    b=input('PASS WORD:')
    try:
        s1="select user_name from user_accounts where password='{}'".format(b)
        c1="select fname,lname from user_accounts where password='{}'".format(b)
        cursor.execute(c1)
        data1=cursor.fetchall()[0]
        
        data1=list(data1)
        data1=data1[0]+' '+data1[1]
        cursor.execute(s1)
        data=cursor.fetchall()[0]
        data=list(data)[0]
        if data==a:
            print(' HII ',data1)
            return True
        else:
            return False
    except:
        print('ACCOUNT DOES NOT EXIST')

def checking_3():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='12345',database='railway')
    cursor=mycon.cursor()
    mycon.autocommit=True
    a=input('USER NAME:')
    b=input('PASS WORD:')
    try:
        s1="select user_name from user_accounts where password='{}'".format(b)
        c1="select fname,lname from user_accounts where password='{}'".format(b)
        cursor.execute(c1)
        data1=cursor.fetchall()[0]
        data1=list(data1)
        data1=data1[0]+' '+data1[1]
        cursor.execute(s1)
        data=cursor.fetchall()[0]
        data=list(data)
        if data[0]==a:
            
            x=['FIRST NAME','LAST NAME','PHONE NUMBER','GENDER','DATE OF BIRTH','AGE']
            s1="select fname,lname,phno,gender,dob,age from user_accounts where password='{}'".format(b)
            cursor.execute(s1)
            data=cursor.fetchall()[0]
            data=list(data)
            print(x[0],':::',data[0])
            print(x[1],':::',data[1])
            print(x[2],':::',data[2])
            print(x[3],':::',data[3])
            print(x[4],':::',data[4])
            print(x[5],':::',data[5])
            
            
        else:
            return False
    except:
        print('ACCOUNT DOES NOT EXIST')

menu()