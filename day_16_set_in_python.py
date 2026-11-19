##create sets
fruits={"apple","banana","apple","mango"}
print(fruits)

#add items
fruits.add("orange")
print(fruits)

##remove items
fruits.discard("banana")
print(fruits)

##set options
a={1,2,3,}
b={3,4,5}
print("union:",a/b)
print("difference:",a&b)
print("symmetric difference:",a^b)



##remove duplicates

cities=['mumbai',"pune","jaipur","jodhpur"]
unique=set(cities)
print("unique cities:",unique)

##missing value
list1={"sql","excel","power bi"}
list2={"sql","power bi"}


missing=list1-list2
print("missing:",missing)

###common skill
deptA={"sql","excel","power bi"}
deptB={"excel","python","power bi"}
print("common skill:",deptA &deptB)