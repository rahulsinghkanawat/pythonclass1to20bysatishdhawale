##create tuple
fruits=("apple","banana","mango")
print(fruits)

#indexing
print(fruits[0])
print(fruits[-1])

#slicing
nums=(10,20,30,40,50,60)
print(nums[1:4])


##looping
colors=("red","blue","green")
for c in colors:
    print(c)


##tuple length
print(len(colors))

#concatenation
a=(1,2)
b=(3,4)
print(a+b)

###packing and unpacking
data=("laptop",4500,"black")
product,price,color=data
print(f"product:{product} price:{price} and color:{color}")


##nested tuples insides list
employees=[("e101","Rohit","Pune"),
           ("e102","priya","Jaipur")]
for eid,name,city in employees:
    print(eid,name,city)