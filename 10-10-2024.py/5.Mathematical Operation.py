#5. Mathematical Operations:
#1.Create two lists of numbers, and use the + operator to concatenate them. Then, use the * operator to repeat the elements of one list 3 times.
l_m=[1,2,3,4,5]
l_m2=[6,7,8,9]

list=l_m + l_m2
print(list)


#2.Given a list of numbers, write a Python program to create a new list where each element is doubled (i.e., each element is multiplied by 2).

l2 = []
for i in l_m:
   result = int(i) * 2
   l2.append(result)

print(l2)


