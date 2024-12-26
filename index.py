import data

myinput = ""

myStart = 0

def welcomePage():
    global myStart
    if myStart == 0:
        print("hello, how can i help you?")
    if myStart == 1:
        print("")
        print("hello again, how can i help you?") 
    
    myStart = 1
    print("1. add user")
    print("2. show all users")
    print("3. find a number")
    print("4. exit")
    print("")
    myinput = input("please enter from list or just numbers: ")
        
    if myinput == "1" or myinput == "add user":
        myname = input("please enter your name: ")
        mynumber = input("please enter your number: ")
        data.insertItem(myname, mynumber)
        print("one item added")

    if myinput == "2" or myinput == "show all users":
        data.showAll()
        welcomePage()
        
    if myinput == "3" or myinput == "find a number":
        myname = input("please enter your name: ")
        data.showUser(myname)
        welcomePage()
        
    if myinput == "4" or myinput == "exit":
        print("have a nice day")
    else:
        print("worng input!")


welcomePage()
