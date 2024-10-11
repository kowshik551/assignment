#6. Membership Operators:
#1.Write a Python program to check if a specific element (e.g., 5) exists in a given list using the in operator. If it exists, print its position; otherwise, print "Element not found."

l_m = [1,2,3,4,5,6]
if 4 in l_m:
    result = l_m.index(4)
    print(result)
else:
    print("Element not found")



#Given a list of student names, check if "John" and "Sara" are in the list using the in operator.

list = ["john","ranjitha","reethu","roshini","ramya","vandhana","sara"]


if "john" and "sara" in list:
    print("yes, both are There")
