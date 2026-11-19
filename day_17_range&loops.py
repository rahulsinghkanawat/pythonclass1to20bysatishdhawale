##day17_range&loops


for i in range(1,6):
    print(i)



for i in range(0,20,2):
    print(i)




for i in range (10,0,-1):
    print(i)


items=["pen","books","laptop"]
for i in range (len(items)):
    print(i,items[i])    


for i in range(1,6) :
    print("emp-",i)  


years=[]
for y  in range (2015,2026):
    years.append(y)
    print(years)


cities=["mUmbai","pune","Jaipur"]
for i in range(len(cities)):
    cities[i]=cities[i].strip().title()
    print(cities)




ids=["emp-001122","emp-550044","emp-114477"]
for i in range(len(ids)):
    print(ids[i][-4:])



for i in range(1,4):
    for j in range(1,10):
        print(f"i value:{i}  j value:{j}")    





        


