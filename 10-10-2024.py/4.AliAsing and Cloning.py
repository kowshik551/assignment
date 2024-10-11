#4. Aliasing and Cloning:
#1.Create a list of numbers. Assign the list to another variable and modify the original list. Check if the second list also changes. Then, create a copy of the original list and show that modifying the copy does not affect the original list.

l_a_c = [1,2,3,4,5,6,7,8,9]
x = l_a_c
print(x)

l_a_c.pop()
print(l_a_c)

print(x)

result = l_a_c.copy()


l_a_c.pop()
print(l_a_c)
print(result)


#2.Write a Python program to demonstrate how changes in a list's alias affect both lists, while changes in a cloned list do not.

l1 = [1,"a",2,"b"]
x = l1

l1.remove(2)
print(l1)
print(x)
print(id(x))
print(id(l1))


list = l1.copy()
print(list)

print(id(list))
print(id(l1))

