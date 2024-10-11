#8. Advanced Challenges:
#1.Create a list of numbers from 1 to 20. Write a Python program to generate two separate lists:
#One containing only the even numbers. 
#Another containing only the odd numbers.

lac=list(range(1,21))
print(lac)
even_i=[]
odd_i=[]
for i in lac:
    if i%2==0:
        even_i.append(i)
    else:
        odd_i.append(i)
print(even_i)
print(odd_i)


#2.Write a Python program that reads a list of integers and returns a new list containing only the unique elements (i.e., removing duplicates).

la=[1,2,3,4,5,5,6,3,2,1,7,3,4,5]
la2=[]
for i in la:
    if i not in la2:
        la2.append(i)
print(la2)

#Given a list of tuples representing (name, age), sort the list by age in ascending order.
list_1=[("ajay",20),("vijay",30),("hari",25),("giri",35)]
print(type(list_1))
sorted_list_1=sorted(list_1, key=lambda x:x[1])
print(sorted_list_1)








