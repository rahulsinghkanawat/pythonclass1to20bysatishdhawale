# #day 12 while loop
# #basic loop
i=1
while i<=10:
    print(i)
    i+=1

#countdown
n=5
while n>0:
    print(n)
    n-=1


#ask user until valid input
num=""
while not num.isnumeric():
    num=input("enter any value:")

    print("number accepted:", num)

#loop through list using while
items=["apple","banana","grapes","orange"]
i=0
while i<len (items):
    print(items[i])
    i+=1


##using break 
x=1
while x<=10:
    if x==5:
        break
    print(x)
    x+=1


#using contine
y=0
while y<10:
    y+=1
    if y%2==0:
        continue
    print(y)    



#password system

password=""
attempts=0
while password!="admin123" and  attempts<3:
    password=input("enter password:")
    attempts+=1
    if password=="admin123":
        print("login successfully")
    else:
        print("wrong password try again, attempts count:",attempts)
        print("3 attemopts expired")