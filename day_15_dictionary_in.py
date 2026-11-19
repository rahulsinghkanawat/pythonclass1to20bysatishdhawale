students={"name":"rohit","age":22,"city":"pune"}
print(students)

##accessing values
print(students["name"])
print(students["city"])

##adding and updating
students["marks"]=85
students["city"]="mumbai"
print(students)

#removing
students.pop("age")
print(students)

###dictionary method
print(students.keys())
print(students.values())
print(students.items())
print(students.get("name"))

###lopping
for k in students:
    print(k,students[k])

###-nested dictonary
employees={
"e101":{"name":"rohit","city":"pune"},
"e102":{"name":"sneha","city":"delhi"}}
print(employees["e101"]["name"])


###mapping wrong -correct
mapper={"mombai":"mumbai",
        "kolkatta":"kolakta"}
print(mapper["mombai"])