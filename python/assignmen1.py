# ⏺️ Question 1 
# Write a Python program to declare variables of different data types such as: 👉

# integer
a=20
print(a)
print("type of a",type(a))

# Float 
b=2.5
print(b)
print("type of b",type(b))

# string
c="Riya Joshi"
print(c)
print("type of c",type(c))

# boolean
d= True
print(d)
print("type of d",type(d))

# ⏺️ Question 2 
# Write a Python program to declare variables of different data types such as:👉

name="riya joshi" 
print(">>>>>..convert into uppercase..<<<<")   # convert in uppercase
print(name.upper())

nme="JAIPUR"
print(">>>>>>..convert into lowercase..<<<<<")    # convert in lowercase
print(nme.lower())

length="hello, My name is riya"
print("length of this string",len(length))  #find the length of string

my_name="rina"
new_name=my_name.replace("n","y")   #replace letter with another letter
print(new_name)


# ⏺️ Question 3 
# Write a Python program to check whether a given word is a palindrome or not using string slicing. 👉
word="malayalam"
print(word[::-1])     #reverse the string



# ⏺️ Question 4 
# Create a list of 10 numbers and perform the following operations:

# Add a new element 
lst=[10,3,5,2,1,15,9,11,8,7]
lst.append(12)
print(lst)

#Remove an element 
lst.remove(12)
print(lst)

# Sort the list 
lst.sort()
print(lst)

# Find the maximum and minimum value 
print(max(lst))
print(min(lst))



# ⏺️ Question 5 
# Write a Python program to count how many even and odd numbers are present in a list. 👉

even=0        #this variable store value
odd=0
for x in lst:
    if x%2==0:
        even += 1    # it is used to count and store value in even variable
    else:
        odd += 1
print(" total even numbers:-",even)
print("total odd numbers",odd)


# ⏺️Question 6 
# Create a tuple containing 5 subjects. Print: 👉

# First element
tpl=("python","java","riya","javascript","sql")  
print("first element:-",tpl[0])          #it is used to find first element of the tuple


# Last element 
print("last element:-",tpl[-1])  #it is used to find last element of the tuple


# Length of the tuple 
print("length of tuple:-",len(tpl))

# Check whether a subject exists in the tuple or not
print("python" in tpl )


# ⏺️ Question 7 
# Write a Python program to create a dictionary of student details containing: 👉

info={"name":"riya",
      "age":21,
      "course":"python",
      "marks":85}
print("keys of dict:-",info.keys())
print("values of dict:-",info.values())


# ⏺️ Question 8 
# Write a Python program to update and delete elements from a dictionary. 👉

info['roll_number']=21    # it is used to update the dictionary
print(info)

info.pop('roll_number')   # it is used to delete the dictionary
print(info)



# ⏺️ Question 9 
# Create two sets and perform the following set operations: 👉

num1={1,2,3,4,5,6}
num2={5,6,7,8,9,0}

print(num1.union(num2))  #union
print(num1.intersection(num2))  #intersection
print(num1-num2)  #difference
print(num1^num2)  #symmetric difference


# ⏺️ Question 10
# Write a Python program to remove duplicate elements from a list using a set. 👉
lst1=[1,2,3,4,4,4,5,6]
dlp_value=list(set(lst1))
print(dlp_value)



