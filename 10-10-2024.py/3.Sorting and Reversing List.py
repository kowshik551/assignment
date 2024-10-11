#3. Sorting and Reversing Lists:
#1.Write a Python program to sort a list of 10 random integers in ascending and descending order using sort() and reverse().

lsr = [1,7,3,6,2,0,8,9,6,5]

lsr.sort(reverse=True)
print(lsr)

lsr.sort()
print(lsr)


#2.Create a list of strings and reverse the order of elements using both reverse() and slicing [::-1]. Compare the results.

lsr.reverse()
print(lsr)