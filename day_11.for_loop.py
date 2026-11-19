#basic loop
for a in range(1,11):
    print(a)

#print characters
word="python"
for alphabet in word:
    print(alphabet)

word2="sql"
for j in range(1,11):
    print(word2)


#loop through list
items =["pen","book","laptop"]
for item in items:
    print(item)

# #even numbers 
print("print odd number:")
for n in range (1,21,2):
    print(n)

# #total calculation
marks=[78,82,90]
total=0
for m in marks:
    total+=m
    print("total:",total)

# #clean city name
cities=["mumbai","pune","chennai"]
cleaned=[]
for c in cities:
    cleaned.append(c.strip().title())
    print(cleaned)

# #loop with if conditions
nums=[5,12,3,18,7]   
for n in nums:
    if n>10:
        print(n,"is greater than 10")
    else:
        print(n,"is not greater than 10") 


#loop with if condition
nums=[5,12 ,3,18,7]
for n in nums:
    if n%2==0:
        print(n,"even number")
    else:
        print(n,"odd number")


# #extract last digits from ids
ids=["EMP-0011122","EMP-889900"]
for last4 in ids:
    print(last4[-4:])                





        





