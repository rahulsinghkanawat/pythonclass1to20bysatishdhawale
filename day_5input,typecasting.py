#input and typecasting
name=input("enter your name:")
print("welcome",name)

age=int(input("enter your age:"))
print(type(age))
age=age+5
print("your age is :",age)

temprature=float(input("enter today's temp:"))
print(type(temprature))

#convert number to string
sales=500000
text="sales:"+str(sales)
print(text)

#total sales calculator
product=input("product name:")
quantity=int(input("enter quantity sold:"))
price_per_unit=float(input("enter price per unit:"))

total_sales=quantity*price_per_unit
print("__________")
print("product",product)
print("total sales amount=",total_sales)

#calculations
first_num=int(input("enter first number"))
second_num=int(input("enter second number"))
sum=first_num+second_num
print(sum)

