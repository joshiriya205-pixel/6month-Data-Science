import os
name=input("enter your name:- ")
last_name=input("enter your last_name:- ")
dob =input("enter your dob:- ")
gender=input("enter your gender:- ")
address=input("enter your address:- ")

os.mkdir(name)
details=[]
details.append("Name: " +name)
details.append("Last_Name: " + last_name)
details.append("Address: " +gender)
details.append("DOB: " +dob)
details.append("address: " +address)
file =open(f"{name}/{name}.txt","w")

file.write("\n".join(details))
file.close()