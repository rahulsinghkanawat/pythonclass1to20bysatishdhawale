# ##learning data types in Python
# #7data types
# text_data_types1
# string

customer_name="Rohit"
print("customer_name is:", customer_name)
print("customer data type is:",type(customer_name))

# # numeric data types
# # 2.1integer_complex number
rating=4
order_quantity=3
print("rating data type",type(rating))
print("order_quantity data type:",type(order_quantity))

# #2.2float_decimal number
order_amount=8599.99
print("order_amount data type:",type(order_amount))

# #2.3complex number
a=3+4j
print(type(a))


# #4.sequence
# #4.1-list
cities=["mumbai","delhi","pune","jaipur"]
print(cities)
print(type(cities))

# ##4.2tuple
dimensions=(1920,1080)
print(dimensions)
print(type(dimensions))

# ##4.3range
num=range(5)
print(list(num)) #[0,1,2,3,4]
print(type(num))

days=range(1,31)  #1 to 30 days
print(type(days))



# ##dictionary(dict)
student={"name":"anvi","age":5, "city":"mumbai"}
print(student)
print(type(student))

# ##6. set
number={1,2,2,3,4}
print(number)   #output={1,2,3,4}
print(type(number))

# ##7.none type-no value
remarks=None
print(remarks,type(remarks))


