#day 9 nested if & multiple conditions
print("check your eligibility") 
age=int(input("enter your age:"))
if age>=18:
    id_no=int(input("enter id no:"))
    if id_no==1722:
        print("you can enter")
    else:
        print("wrong id num")    
else:
    print("you are underage")        




####multiconditions and uses
age=int(input("enter your age:"))    
residence=input("are you indian:")
if age>=18 and residence=="yes":
    print("eligible to drive")
else:
    print("not eligible to drive")    




####multiple condition or uses
age=int(input("enter your age:"))
residence=input("do you have licence;")
if age>=18 or residence.lower()=="yes":
    print("eligible to drive")
else:
    print("not eligible to drive")    