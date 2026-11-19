##assignment
employee_name=input("enter employee name:")
basic_salary=float(input("enter basic salary:"))
bonus=float(input("enter bonus amount:"))
tax_ercentage=float(input("enter tax percentage:"))
gross_salary=basic_salary+bonus
tax_amount=(gross_salary*tax_ercentage)/100
net_salary=gross_salary-tax_amount

print("employee name:",employee_name)
print("basic salary:",basic_salary)
print("bonus amount:",bonus)
print("gross salary:",gross_salary)
print("tax percentage:",tax_ercentage,"%")
print("tax amount:",tax_amount)
print("net salary:",net_salary)


