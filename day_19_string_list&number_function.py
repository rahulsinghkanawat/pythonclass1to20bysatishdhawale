###day 19 string function & number functions

text="banana"
print(text.count("a"))

print("hello.py".endswith(".py"))


print("sales_report.csv".startswith("sales"))

print("1245435454354".isdigit())
print("abc".isalpha())
print("rahul2004radhe".isalnum())
print("line1\n line2\n line3")
print("line1\n line2".splitlines())



##list functions
nums=[4,5,6,3,6,]
nums.sort()
print(nums)



fruits=["banana","apple","mango"]
print(sorted(fruits))


marks=[10,20,30]
print(min(marks),max(marks),sum(marks))


mylist=[1,2,3,4,1,2]
print(mylist.count(1))
print(mylist.index(4))





a=[1,2]
b=[3,4]
a.extend(b)
print(a)



##number  funtions
print(round(3.678,2))
print(abs(-50))
print(pow(3,4))
print(divmod(10,3))
print(sum([5,5,5],5))



#####practical example
products=["mobile","laptop","tablet"]
clean=[p.strip().title() for p in products]
clean.sort()
print(clean)


emails=["rohit2gmail.com","rahul@gmail.com"]
domains=[mail[mail.find("@")+1:]for mail in emails]
print(domains)



mobiles=["9672758405","54785495847ggj","8749"]
valid=[m for m in mobiles if m.isdigit()and len (m)==10]
print(valid)


