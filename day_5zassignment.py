#assignment
item=input("enter item name:")
price=float(input("original price;"))
discount=float(input("discont percentage:"))
discount_amount=price*discount/100
final_price=price-discount_amount
print("final price of",item,"=",final_price)