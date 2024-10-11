#2. Adding and Removing Elements:
#1.Write a Python program that initializes a list with some numbers:

l_a_r = list(range(1,7))
print(l_a_r)

#2.Adds a new number to the list using the append() method.

l_a_r.append(7)
print(l_a_r)

#3.Inserts a number at the second position using insert().

l_a_r.insert(1,7)
print(l_a_r)

#4.Extends the list with another list of numbers.

l_a_r_2=[10,9,8,7,6]
l_a_r_2.extend(l_a_r)

#5.Remove all occurrences of the number 3 from a list of integers.

print(l_a_r_2)
l_a_r_2.remove(3)
print(l_a_r_2)

#6.Write a Python program to remove the last element of a list using pop() and print the updated list.
l_a_r.pop()
print(l_a_r)



