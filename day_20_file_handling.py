###day20 file handling

##reading full file
with open("day_20sample.text","r")as f:
    print(f.read())



###reading line by line
with open("day_20sample.text","r")as f:    
    for line in f:
        print(line.strip().title())    



###writing
with open("notes.text","w")as f:
    f.write("day_20 -file handling\n")
    f.write("learning read and  write.\n")


####appending
with open("notes.text","a")as f:
    f.write("appending new content.\n")



####cleaning data in file
cleaned=[]
with open("day_20sample.text","r") as f:
    for line in f:
        cleaned.append(line.strip().title())
        with open("cleaned_output.text","w") as f:
            for city in cleaned :
                f.write (city+"\n") 




###counting lines
count=0
with open ("day_20sample.text","r")as f:
    for _ in f:
        count +=1
        print("total lines:",count)                         