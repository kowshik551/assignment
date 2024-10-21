<<<<<<< HEAD
#LIST:-

#Write a python program to merge two list?
list1_1=input("Enter list1_1 : ")
list1_2=input("Enter list!_2 : ")
list1=list1_1+list1_2
print(list1)

#Write a python program to delete element of given index in list ?
list2=["apple","car","banana","mango","kiwi","cherry"]
list2.remove("car")
print(list2)

#Write a pytho program to delete given element from the list?
list3=["apple","car","banana","mango","kiwi","cherry"]
list3.remove("kiwi")
print(list3)

#Write a python programe to check if the two list are having atleast one common element?

l4_1=[1,2,3,4,5]
l4_2=[5,6,7,8,9]
result = set(l4_1).intersection(set(l4_2))
print(list(result))

#Write a python program to remove specified column from the nestedlist?

list =[[1,2,3],[4,5,6],[7,8,9]]
for i in list:
    del i[0]
print(list)

#Write python program to convert a list of integers into single integer ?
list6=[1,2,3,4,5,6]
print(sum(list6))

#Write a python programe to remove duplicates from the list ?

list7_1=[1,2,3,4,5,6,4,3,7]
print(list(set(list7_1)))
print(type(list7_1))


#SET:-

#Write a program to create a set.
s1_1=input("Enter a values : ")
s1=set(s1_1)
print(s1)

#Write program to iterate over sets.
for i in s1:
    print(i, end=" ")

#Write a Python program to add member to a set.
s2={1,2,3,4,5,6}
s2.add(10)
print(s2)

#Write a Python program to remove item from a given set.
s3=s2
print(s3)
s3.pop()
print(s3)

#Write a python program to create a intersection of set ?

#Intrtaction: It returns common elements from both sets.

s4_1={10,20,30,40,50}
s4_2={10,20,30,60,70}
s4=s4_1&s4_2
print(s4)

#Write a python program to createa union of set ?

# Union: it reyturns both sets.

s5_1={10,20,30,40,50}
s5_2={60,70,80,90,100}
s5=s5_1|s5_2
print(s5)

#Write a python program to create set differance ?
s6_1={10,20,30,40,50}
s6_2={40,50,60,70,80}
s6=s6_1-s6_2
print(s6)

#Write a python program to create a symmetric defferance ?
s7_1={1,2,3,4,5,6}
s7_2={5,6,7,8,9}
s7=s7_1^s7_2
print(s7)

#write a python program to find max and min values in a set?

s8={1,2,3,4,5,6,7,8,10,29}
print(min(s8))
print(max(s8))

#Given two Python sets, write a Python program to update the first set with items that exist only in the first set and not in the second set.

s9={"apple","cherry","mango"}
s9_1={1,2,3,4,5}
s9.update(s9_1)
print(s9)

#Write a Python program to remove items 10, 20, 30 from the following set at once.?

s10_1={10,20,30}
s10_1.clear()
print(s10_1)

#Check if two sets have any elements in common. If yes, display the common elements?

s1 = {1,2,3,4,5,6,34,657,789}
s2 = {1,2,3,4,763,9873.98734}


if s1.isdisjoint(s2):  #we use isdisjoin() method to check uncomon elements or not
    print("no comon elements")
else:
    print(s1.intersection(s2))

#Remove items from set1 that are not common to both set1 and set2?

s13_1={1,2,3,4,5,6,6,7,8,9}
s13_2={1,3,5,10,21,30,5,7}
s13=s13_1.intersection_update(s13_2)
print(s13)

#TUPLE:-

#How do you create a empty tuple on python ?
t1=tuple()
print(t1,type(t1))

#Write a python program to unpack a tuple into several variables ?

t2=("apple","banana","mango","kiwi")
(s1,s2,s3,s4)=t2
print(s1)
print(s2)
print(s3)
print(s4)

#write a python program to add an item to the tuple ?

t3=("apple","lemon","apricot","plum","peaches","pears")
t3_1=list(t3)
t3_1.append("papayas")
t3=tuple(t3_1)
print(t3)

#Write a python proram to convert tuple into a string ?

t4=("apple","lemon","apricot","plum","peaches","pears")
str_1=str(t4)
print(str_1,type(str_1))

#DICTIONARY:-

#Write a python program to  add a key to a dictionary ?

dict1={"Brand":"Ford","Model":"Mustang","Year":1964}
dict1["color"]="red"
print(dict1)

#Write a python program to check weather the given value is present in the dictionary or not ?

dict2={"Brand":"Ford","Model":"Mustang","Year":1964}
if "Mustang" in dict2.values():
    print("Yes, it exist")
else:
    print("No, Not exist")

#Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
#Sample Dictionary
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
dict3={}
for x in range(1,16):
    dict3[x]=x**2
print(dict3)

#Write a python program to merge two python dictionaries ?

dict6={"Kohli":90,"Rohit":65,"Gill":35,"Suryakumar":50,"Bumrah":30}
dict6_1={"Rahul":100,"Shreyes":70,"Siraj":25,"Kihan":60,"Shami":20,"Ashwin":25}
dict6.update(dict6_1)
print(dict6)

#Write a Python program to create a dictionary from a string.  Note: Track the count of the letters from the string.
#Sample string : 'skywavessoftwares'
#Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

dict7={}
s="skywavessoftwares"
for letter in s:
    dict7[letter]=dict7.get(letter,0)+1
print(dict7)


=======
#LIST:-

#Write a python program to merge two list?
list1_1=input("Enter list1_1 : ")
list1_2=input("Enter list!_2 : ")
list1=list1_1+list1_2
print(list1)

#Write a python program to delete element of given index in list ?
list2=["apple","car","banana","mango","kiwi","cherry"]
list2.remove("car")
print(list2)

#Write a pytho program to delete given element from the list?
list3=["apple","car","banana","mango","kiwi","cherry"]
list3.remove("kiwi")
print(list3)

#Write a python programe to check if the two list are having atleast one common element?

l4_1=[1,2,3,4,5]
l4_2=[5,6,7,8,9]
result = set(l4_1).intersection(set(l4_2))
print(list(result))

#Write a python program to remove specified column from the nestedlist?

list =[[1,2,3],[4,5,6],[7,8,9]]
for i in list:
    del i[0]
print(list)

#Write python program to convert a list of integers into single integer ?
list6=[1,2,3,4,5,6]
print(sum(list6))

#Write a python programe to remove duplicates from the list ?

list7_1=[1,2,3,4,5,6,4,3,7]
print(list(set(list7_1)))
print(type(list7_1))


#SET:-

#Write a program to create a set.
s1_1=input("Enter a values : ")
s1=set(s1_1)
print(s1)

#Write program to iterate over sets.
for i in s1:
    print(i, end=" ")

#Write a Python program to add member to a set.
s2={1,2,3,4,5,6}
s2.add(10)
print(s2)

#Write a Python program to remove item from a given set.
s3=s2
print(s3)
s3.pop()
print(s3)

#Write a python program to create a intersection of set ?

#Intrtaction: It returns common elements from both sets.

s4_1={10,20,30,40,50}
s4_2={10,20,30,60,70}
s4=s4_1&s4_2
print(s4)

#Write a python program to createa union of set ?

# Union: it reyturns both sets.

s5_1={10,20,30,40,50}
s5_2={60,70,80,90,100}
s5=s5_1|s5_2
print(s5)

#Write a python program to create set differance ?
s6_1={10,20,30,40,50}
s6_2={40,50,60,70,80}
s6=s6_1-s6_2
print(s6)

#Write a python program to create a symmetric defferance ?
s7_1={1,2,3,4,5,6}
s7_2={5,6,7,8,9}
s7=s7_1^s7_2
print(s7)

#write a python program to find max and min values in a set?

s8={1,2,3,4,5,6,7,8,10,29}
print(min(s8))
print(max(s8))

#Given two Python sets, write a Python program to update the first set with items that exist only in the first set and not in the second set.

s9={"apple","cherry","mango"}
s9_1={1,2,3,4,5}
s9.update(s9_1)
print(s9)

#Write a Python program to remove items 10, 20, 30 from the following set at once.?

s10_1={10,20,30}
s10_1.clear()
print(s10_1)

#Check if two sets have any elements in common. If yes, display the common elements?

s1 = {1,2,3,4,5,6,34,657,789}
s2 = {1,2,3,4,763,9873.98734}


if s1.isdisjoint(s2):  #we use isdisjoin() method to check uncomon elements or not
    print("no comon elements")
else:
    print(s1.intersection(s2))

#Remove items from set1 that are not common to both set1 and set2?

s13_1={1,2,3,4,5,6,6,7,8,9}
s13_2={1,3,5,10,21,30,5,7}
s13=s13_1.intersection_update(s13_2)
print(s13)

#TUPLE:-

#How do you create a empty tuple on python ?
t1=tuple()
print(t1,type(t1))

#Write a python program to unpack a tuple into several variables ?

t2=("apple","banana","mango","kiwi")
(s1,s2,s3,s4)=t2
print(s1)
print(s2)
print(s3)
print(s4)

#write a python program to add an item to the tuple ?

t3=("apple","lemon","apricot","plum","peaches","pears")
t3_1=list(t3)
t3_1.append("papayas")
t3=tuple(t3_1)
print(t3)

#Write a python proram to convert tuple into a string ?

t4=("apple","lemon","apricot","plum","peaches","pears")
str_1=str(t4)
print(str_1,type(str_1))

#DICTIONARY:-

#Write a python program to  add a key to a dictionary ?

dict1={"Brand":"Ford","Model":"Mustang","Year":1964}
dict1["color"]="red"
print(dict1)

#Write a python program to check weather the given value is present in the dictionary or not ?

dict2={"Brand":"Ford","Model":"Mustang","Year":1964}
if "Mustang" in dict2.values():
    print("Yes, it exist")
else:
    print("No, Not exist")

#Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
#Sample Dictionary
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
dict3={}
for x in range(1,16):
    dict3[x]=x**2
print(dict3)

#Write a python program to merge two python dictionaries ?

dict6={"Kohli":90,"Rohit":65,"Gill":35,"Suryakumar":50,"Bumrah":30}
dict6_1={"Rahul":100,"Shreyes":70,"Siraj":25,"Kihan":60,"Shami":20,"Ashwin":25}
dict6.update(dict6_1)
print(dict6)

#Write a Python program to create a dictionary from a string.  Note: Track the count of the letters from the string.
#Sample string : 'skywavessoftwares'
#Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

dict7={}
s="skywavessoftwares"
for letter in s:
    dict7[letter]=dict7.get(letter,0)+1
print(dict7)


>>>>>>> 1d0c83e4e50b80dfb34b836d0dd7a4b527fd13bd
