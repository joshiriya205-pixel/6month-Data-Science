# #print("hello hii kese ho 😊😂")
# name = "riya"
# print(name)

# age=20
# Age=20
# AGE=20
# print(age)
# print(Age)
# print(AGE)


# >>>>>>>>>>>>>>string datatype in python 
# name="upflairs"
# # print("this is my first string :-",name)
# # print("this is my first string :-",type(name)) ## type function show data type
# # num="1234"
# # print(num)
# # print("this is my first string :-",type(num))
# # print("len of my first string",len(name)) ###find the len of my string

# # #indexing & slicing
# # print(name[0])
# # print(name[2])
# # print(name[3])
# # print(name[4])

# print("Slicing:-",name[0:4])
# task1 reverse the string
# print(name[::-1])

# company_name= "upflairs pvt ltd"
#loweer case convert into upper case
# upper_case=company_name.upper()
# print("upper case 😊😊",upper_case)

#upper case convert into lower case
# company_name= "UPFLAIRS PVT LTD"
# # lower_case=company_name.lower()
# # print("lower case ",lower_case)

# lower_case=company_name.casefold()###task2
# print(lower_case)

# company_name="upflairs pvt ldt"
# # print(company_name.title()) ## every word  first letter of string capital
# print(company_name.capitalize()) ## first word of the string first letter capital


# name= "riya"
# c= name.count('i')
# print(c)


# print(name.index('y'))

# name ="riya"
# last_name="joshi"
# print("add two string:-",name+ last_name)
# print("add two string:-",name,last_name)
# print("add two string:-",name+" "+ last_name)



# name ="riya "
# # last_name="joshi"
# # print(name+last_name)
# # print(name*last_name)
# # print(name/last_name)
# # print(name**last_name)

# print(name*2)

# intro = """Hi, I am Riya Joshi. I am a second-year B.Tech CSE student with an interest in web development and programming. I know HTML, CSS, and JavaScript, and I am currently learning Data Structures and Algorithms. I have also completed DSA training and enjoy improving my technical skills. I am hardworking, eager to learn new technologies, and want to build a successful career in the IT field."""

# print(intro)


# name="riya"
# print(f"my name is {name} and i am from jaipur")


# path= r"file:///C:/Users/RIya/Documents/DAA%20lab.pdf"
# print(path)



#>>>>>>>>>>>list data type
# it is hetrogeneous
# mutable
# lst=[1,2,2,3,4,5, "riya",2.3,"😊😊😊"]
# print("this is my first list",lst)
# print("type of my list:-",type(lst))
# print("length of the list" ,len(lst))

# print("indexing and slicing:->>>")

# lst=[1,2,2,3,4,5, "riya",2.3,"😊😊😊"]
# print(lst[0])
# print(lst[1])
# print(lst[5])
# print(lst[6])

# print("slicing>>>>:-")
# print(lst[0:3])
# print(lst[2:5])
# print(lst[5:8])

# lst=[1,2,2,3,4,5, "riya",2.3,"😊😊😊"]
# # lst.append("upflairs") ##add the value at the last of the list 
# # lst.insert(0,"upflairs") ## add value anywhere using index no.
# # lst.remove(1) ## remove the element at specific position
# # lst.pop(5)
# lst.extend([1,0])
# # lst.clear()
# lst.copy()
# print(lst)

# lst1=[1,2,2,3,4]
# lst2=[5,6,7,8,9]
# print(lst1+lst2)

# max()
# min()
# sum()
# len()

# # for update
# lst=[1,4,4,4,3,2,6]
# # lst[0]="hello"
# # lst.sort()
# # print(min(lst))
# # print(max(lst))
# # print(len(lst))
# # print(sum(lst))
# # print(lst.count(4))
# # lst.reverse()
# print(lst)


# # >>>>>>>>...tuple...<<<<<<<<<<
# # # A tuple in Python is an ordered collection of elements, It can store different types of data together,  Tuples are immutable, which means their values cannot be changed,Tuples are written using round brackets ().
# # Key Points:
# # Stores multiple values
# # Ordered collection
# # Allows different data types (heterogeneous)
# # # Immutable (no add/remove/change)

# tpl=(1,2,3,4,4,4,5,"hii","riya",4.5,"❤️❤️")
# print("this is my first tuple:-",tpl)
# print("type of my first tuple:-", type(tpl))
# print("len of my first tuple:-", len(tpl))


# print(">>>>>>>>indexing and slicing<<<<<<")
# print(tpl[0])
# print(tpl[1])
# print(tpl[2])
# print(tpl[3])
# print(tpl[4])
# print(tpl[2:5])

# print( tpl.count(4))
# print(tpl.index(5))

# a=1,2,3,"hello","hii"    ## it is work as tuple by default
# print(a)
# print(type(a))
# print(len(a))


# print(">>>>>>>tuple unpacking python<<<<<<<")
# a,b,c=(1,2,3)
# print(a)
# print(b)
# print(c)

# print(">>>>>>>tuple unpacking python<<<<<<<")
# a,b=(1,2,3)
# print(a)
# print(b)


# typecasting:-ek datatype se another datatype me convert krna



# tpl=(1,2,3,4,4,4,5,"hii","riya")
# print("this is my tuple:-",tpl)
# print("type of my tuple:-",type(tpl))

# print(">>>>>tuple convert into list<<<<<<<<")
# lst=list(tpl)
# print("this is my list:-",lst)
# print("type of my liste:-",type(lst))
# print("----->>>>>add item in list<<<<")
# lst.append("item add")
# print("items are added:-",lst)
# print("---->>>>list convert into tuple<<<")
# tpl=tuple(lst)
# print("this is my tuple:-",tpl)
# print("type of my tuple:-",type(tpl))
# print("items are added in tuple") 


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>dict
# dict it is keyword of dict
# pair of key and value(items)
student={"name":"riya",
         "class":"3rd year",
         "subject":"python",
         "rollnumber":28,
         "branch":"CSE"}
# print(student)
# print(student.keys())
# print(student.values())
# print(student.items)


# print(student['name'])
# print(student['class'])
# print(student['branch'])
# print(student['rollnumber'])


# print(student.get('name'))
# print(student.get('branch'))
# print(student.get('rollnumber'))
# print(student.get('class'))

print(student.pop('name'))

# car={"brand":"honda",
#      "model":2025,
#      "owner":"second owner"}
# x=car.setdefault('color','white')
# print(x)

# car['car name']="BMW"
# print(car)

# car['model']=2026
# print(car)



# car={"brand":"honda",
#      "model":2025,
#      "owner":"second owner",
#      "car name":["Honda City",
#  "Honda Amaze",
#  "Honda Elevate",
#  "Honda Jazz",
#  "Honda Brio",
# " Honda Civic",
# " Honda Accord",
#  "Honda WR-V",
# " Honda CR-V",
#  "Honda City e:HEV",
#  "Honda e"]}
# print(car['car name'])


# for x in car.keys():
#     print(x)

# for x in car.values():
#     print(x)    


# for x in car.items():
#     print(x)



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>...SET

# A set is a well-defined collection of distinct objects or elements.
# Sets are usually represented using curly brackets { }.


# sat={1,2,3,4,5}
# # print("this is my set:-",sat)
# # print("len of my set:-",len(sat))
# # print("type of my set:-",type(sat))

# # sat.add(10)
# # print(sat)

# # sat.remove(1)    #it show error when value not present in set

# sat.discard(10)  #it not show error when value not present in set
# print(sat)


s1={1,2,3,4,5}    
s2={3,4,5,6}
# print(s1|s2)
# result=s1.union(s2)   #add two sets
# print(result)

# # print(s1&s2)
# result=s1.intersection(s2) # same values of two sets
# print(result)

# print(s1-s2) #different value from s2 set
print(s1^s2)

# a={1,2}
# b={1,2,3,4}

# print(b.issuperset(a))
# print(a.issubset(b))











