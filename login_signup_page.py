import json
import os
import re
file=os.path.exists("Login_System_Data.json")
if file==False:
    print("Login page:-")
    myRL=input("choose signup or login: ")
    if myRL == "signup":
        Username = input("inter your Username:") 
        Pno=input("enter your pno:") 
        description = input("description:") 
        age=int(input("enter your age:-"))
        PW = input(" enter your Password:")
        if re.fullmatch(r'[A-Z a-z 0-9 @#$%^&*+=]{8,}',PW):
            print("strong password")
            PW1 = input("Confirm Passwor:-")
            dic={"Username":Username,"Pno": Pno,"description":description,"PW":PW,"age":age,"PW":PW}
            list=[]
            list.append(dic)
            if(PW == PW1):
                print("Registration successfully.")
                with open('Login_System_Data.json', 'w',) as f:      
                    json.dump(list,f,indent=4,)
        else:
            print("Registration failed! Please confirm your Password correctly.") 
elif file==True:
    myRL=input("choose signup or login: ")
    if myRL == "signup":
        Username = input("enter your Username:") 
        Pno=input("enter your pno:") 
        description = input("description:") 
        age=int(input("enter your age"))
        PW = input(" enter your Password:")
        if re.fullmatch(r'[A-Z a-z 0-9 @#$%^&*+=]{8,}',PW):
            print("strong password")
        PW1 = input("Confirm Passwor",)
        dic={"Username":Username,"Pno": Pno,"description":description,"PW":PW,"age":age,"PW":PW}
        with open('Login_System_Data.json', 'r') as f1: 
            list=json.load(f1)
        list.append(dic)
        if(PW == PW1):
            print("Registration successfully.")
            with open('Login_System_Data.json', 'w',) as f:      
                json.dump(list,f,indent=4,)
        else:
            print("Registration failed! Please confirm your Password correctly.") 
    elif myRL == "login":
        User = input(" enter your Username:") 
        PW = input("Password:")
        with open('Login_System_Data.json', 'r') as f: 
            b = json.load(f)
        def login_or_not(PW ,b) :
            for i in b:
                for j in i:
                    if j=='PW' :
                        if i[j]==PW:
                            print(i)
                            return i
        data=login_or_not(PW,b)
        if data:
            print("login successfully")
        else:
            print("Login failed. Wrong Username or Password .")   
else:               
    print("wrong info")


