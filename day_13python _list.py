#create list
fruits=["apple","banana","mango"]
print(fruits)


#indexing
fruits=["apple","banana","mango"]
print(fruits[0])
print(fruits[-1])

#update list
fruits=["apple","banana","mango"]
fruits[1]="orange"
print(fruits)

#add items
fruits=["apple","banana","mango"]
fruits.append("graps")
print(fruits)

fruits.insert(1,"papaya")
print(fruits)

#####remove items
fruits=["apple","banana","mango"]
fruits.remove("mango")
print(fruits)

#slicing
nums=[10,20,30,40,50,60]
print(nums[1:3])
print(nums[-3:])

##looping
fruits=["apple","banana","mango"]
for f in fruits:
    print("fruits:",f)

#clean city name
raw=["mUMBAi","delhi","pune"]
clean=[]
for c in raw:
    clean.append(c.strip().title())
    print(clean)

    ##replace wrong spellings
wrong=["kolkatta","dehi"]
fixed=[]
for c in wrong:
    c= c.replace("kolkatta","kolkata").replace("dehi","delhi")
    fixed.append(c)
    print(fixed)


##extract years
codes=["laptop-2026","phone-2027"]
years=[]
for c in codes:
    years.append(c[-4:])
    print(years)
         

