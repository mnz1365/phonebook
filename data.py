import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mnz1986",
  database="mnzdb"
)

# add phone number
def insertItem(myname, mynumber) :
    
    mycursor = mydb.cursor()
    sql = "INSERT INTO phonebook (phonebookname, phonebooknumber) VALUES (%s, %s)"
    val = (myname, mynumber)
    mycursor.execute(sql, val)
    
    mydb.commit()
    
    print(mycursor.rowcount, "record inserted.")

#show all phone number
def showAll():
     mycursor = mydb.cursor()
     sql = "SELECT * FROM phonebook"
     mycursor.execute(sql)
     myresult = mycursor.fetchall()
     
     for x in myresult:
         print(x)
         

#show user if exist
def showUser(user):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM phonebook WHERE phonebookname = %s"
    usr = (user, )
    
    mycursor.execute(sql, usr)
    
    myresult = mycursor.fetchall()
    
   
    if len(myresult) == 0:
        print("sorry, no user found!!!")
        
    if len(myresult) > 0:

        print("user found...")
        for x in myresult:
            print(x)
    

     