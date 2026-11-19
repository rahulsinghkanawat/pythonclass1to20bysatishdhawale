#string method very important

text="        hello python developer         "
#removes spaces
print("original text:",text)
print("remove spaces:",text.strip())

#convert to capital letters
text="        hello python developer         "
print("capital letters:",text.upper().strip())



#convert to proper case
text="        hello python developer         "
print("proper letters:",text.title().strip())



#convert to lower case
text="        hello python developer         "
print("lower letters:",text.lower().strip())



#replace
text="        hello python developer         "
print("replace python word with sql",text.replace("python","sql"))

#count occurences of a letters of word
text="        hello python developer         "
print("count of o",text.count("o"))

#check if text start with something
text="        hello python developer         "
print("starts with hello",text.strip().startswith("hello"))



#check if only number are present in data 
mobile="9672758405"
print("is numeric:",mobile.isnumeric)



msg="welcome to python course"
#split string into list of words
word=msg.split()
print("word list:",word)

#join back with hyphen
joined_text="-".join(word)
print("joined text:",joined_text)

#find position of letters
msg="welcome to python course"
print("index of p:",msg.find("p"))

#extract domain
email=("student@example.com")
domain=email[email.find("@")+1:]
print("domain:",domain)



