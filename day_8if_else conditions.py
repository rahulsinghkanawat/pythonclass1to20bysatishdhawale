age=int(input("enter your age:"))
if age>=18:
    print("voting qualify")
else:
    print("not qualify for voting")

#discount checker
amount=1500
if amount>=1000:
    print("you get a descount!")
else:
    print("no discout")  


#if elif else 
marks=int(input("enter your marks:"))
if marks>=90:
    print("grade a")

elif marks>=75:
    print("grade b")

elif marks>=33:
    print("grade c")  

else:
    print("fail")          



#sales performance
sales=65000
if sales>=10000:
    print("high performer")
elif sales>=50000:
    print("medium performance")
else:
    print("low performance")

#  string comparison 
city="Delhi"
if city.lower()=="delhi":
    print("city matched")
else:
    print("city not matched")   


password=input("enter your password")
if password=="Admin@2004":
    print("login successfully")
else: 
    print("wrong password")    


# #email validation
email="user@example.com"
if"@"in email and "."in email:
    print("valid email")
else:
    print("invalid email")    



##advanced missing data check
value="Radhe"
if value==" ":
    print("missing data available")
else:
    print("data found")    

