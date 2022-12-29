import mysql.connector
import random
import matplotlib.pyplot as plt

#CONNECTION BETWEEN FRONT_END AND BACK_END

mycon=mysql.connector.connect(user='root',password='1234Abbu',host='localhost',charset='utf8')

cursor=mycon.cursor()
cursor.execute("create database if not exists QUIZ")
cursor.execute("use Quiz")
cursor.execute("create table if not exists SIGNIN(Player_Name char(14),Roll_No int(11) primary key,Class int(4),Pwd int(20))")
cursor.execute("create table if not exists Question(q_no int(4),Question varchar(200) primary key,Option1 varchar(50),Option2 varchar(50),option3 varchar(52),Answer varchar(50))")
cursor.execute("create table if not exists Score(Roll_No int(11), Points int(11))")
#cursor.execute("create table if not exists result(foreign key(Question_no)references Q(Question_No),Question_no int(4) primary,Correct_Ans int(4),percentage float(30)")
f=0

while(True):
    if f==0:
        print("\t\t     _____           ___ ___  ______   ")
        print("\t\t    |     |  |     |     |         /   ")
        print("\t\t    |     |  |     |     |        /    ")
        print("\t\t    |   \ |  |     |     |       /     ")
        print("\t\t    |    \|  |     |     |      /      ")
        print("\t\t    |_____\  |_____|  ___|___  /______ ")
        
        print("")
        print("\t\t 1.REGISTER YOURSELF")
        print("\t\t 2.LOG IN and PLAY QUIZ")
        print("\t\t 3.SCORE")
        print("\t\t 4.ADMIN-LOGIN")
        print("\t\t 5.PLOT SCORE GRAPH")
        
        ch=int(input("ENTER YOUR CHOICE: "))
    
#PROCEDURE FOR SIGN UP

    if(ch==1):
        pname=input("PLAYER-NAME: ")
        roll=int(input("ID/ROLL-NO: "))
        c=int(input("CLASS: "))
        pwd=int(input("PASSWORD: "))
        pwd1=int(input("RE-ENTER PASSWORD: "))
        if pwd==pwd1:
            cursor.execute("insert into SIGNIN(Player_Name,Class,Roll_No,Pwd) values('{}',{},{},{})".format(pname,c,roll,pwd))
            cursor.execute("insert into Score(Roll_No,Points) values({},{})".format(roll,0))
        else:
            print("\t\t **Terminate Program, start again and SIGN IN yourself**")
        mycon.commit()
        print("\t\t\t ***ID REGISTERED***")

#PROCEDURE FOR LOGIN   

    if(ch==2):
        print("\t\t\t ****LOGIN and PLAY QUIZ****")
        roll=int(input("ID/Roll NO: "))
        pwd2=int(input("ENTER YOUR USER PASSWORD: "))
        cursor.execute("select * from signin where roll_no={} and Pwd={}".format(roll,pwd2))
        d=cursor.fetchall()
        a=cursor.rowcount
        #print(a)
        if a>0:
            
            s=int(input("How Many Question Do you want to Play: "))
            i=0
            c=0
            x=0
            l=[]
            print("\t **************QUIZ*************\t")
            while i<s:
               
                cursor.execute("select * from Question ")
                b=cursor.fetchall()
                b=cursor.rowcount
                x=random.randint(1,b)
                
                if x in l:
                    
                    continue
                else:
                    l.append(x)
                    cursor.execute("select question,Option1,Option2,option3,Answer from Question where q_no={}".format(x))
                    d=cursor.fetchall()
                
                    print(d[0][0])
                    print(" ")
                    print("option a: ",d[0][1])
                    print(" ")
                    print("option b: ",d[0][2])
                    print(" ")
                    print("option c: ",d[0][3])
                    print(" ")
                    ans=(input("ENTER YOUR ANSWER: "))
                    if ans==d[0][4]:
                        print("YOUR ANSWER IS CORRECT")
                        c=c+1
                    else:
                        print("YOUR ANSWER IS WRONG")
                        print("")
                        print("CORRECT ANSWER IS" ,d[0][4])
                        print("")
                        print("BETTER LUCK FOR NEXT TIME")
                    i=i+1
                print("")
                print("You got",c,"Points out of",s)
                cursor.execute("update Score set points={} where Roll_no={}".format(c,roll))
                mycon.commit()
        else:
            break
            print("")
            print("\t\t\t PASSWORD IS INCORRECT")
          
    #Player Score          
    
    if(ch==3):
        print("\t\t\t &&&SCORE$$$")
        print(" ")
        roll=int(input("ID/Roll NO: "))
        pwd2=int(input("Enter your USer Password: "))
        cursor.execute("select * from Score where Roll_no={} ".format(roll))
        d=cursor.fetchone()
        print("Your Total Score: ",d[1])
        
     #INSERTING DATA BY ADMIN 
    
    if(ch==4):
        print("\t\t\t Admin-LOGIN ")
        ADMINId=int(input("ADMIN-ID(int): "))
        pname=input("PLAYER-NAME: ")
        PASS=int(input("PASSWORD: "))
        pname1="admin"
        PASS1=1234
        if PASS==PASS1:
            c=int(input("CLASS: "))
            #pwd=int(input("PASSWORD (IN NUMERIC):"))
            #pwd1=int(input("RE-ENTER PASSWORD :"))
            cursor.execute("select * from Question ")
            cursor.fetchall()
            b=cursor.rowcount
            #if b>0:
            y=int(input("How Many Question Do you want to Add:"))
            j=0
            while j<y:
                #qno=int(input("QUESTION NO:"))
                quest=input("ENTER NEW QUESTION: ")
                op1=input("OPTION a: ")
                op2=input("OPTION b: ")
                op3=input("OPTION c: ")
                ans=input("Ans a,b,c: ")
                j=j+1
            
                cursor.execute("insert into Question(q_no,Question,Option1,Option2,option3,Answer) values({},'{}','{}','{}','{}','{}')".format(b+1,quest,op1,op2,op3,ans))
                #cursor.execute("insert into Score(Roll_No,Points) values({},{})".format(roll,0))
                b=b+1
                mycon.commit()
        else:
            print(end="Terminate Program, WRONG PASSWORD")


    if(ch==5):
        cursor.execute('select Roll_No,Points from score')
        rollno = []
        points = []
  
        for i in cursor:
            rollno.append(i[0])
            points.append(i[1])
            
        plt.bar(rollno,points)
        plt.xlabel('Roll No')
        plt.ylabel('Points')
        plt.show()
        
