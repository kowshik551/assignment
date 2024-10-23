<<<<<<< HEAD
# MAP Function():

def add_2(x):
    x+=2
    return x
num_list=[1,2,3,4,5,6]
print("original list is : ", num_list)
new_list=(list(map(add_2,num_list)))
print("modified list is : ", num_list)



# Reduce () Function:
from functools import reduce
def add(x,y):
    return x+y
num_list = [1,2,3,4,5]
print("sum of values in list = ")
print(reduce(add, num_list))

#filter () Function :
def check(x):
    if (x % 2 == 0 or x % 4 == 0):
        return 1
evens = list(filter(check,range(2,22)))
print(evens)



#1. Write a Python function to find the maximum of three numbers.

def max_of_three(a,b,c):
    return max(a,b,c)
a=20
b=39
c=32
operation = max_of_three
print(max_of_three(a,b,c))


#2. Write a Python function to sum all the numbers in a list.
#Sample List : (8, 2, 3, 0, 7)
#Expected Output : 20

def sum_of_numbers():
    total= sum_of_numbers
    return total
total=8,2,3,0,7
print(sum(total))

#3. Write a Python function to multiply all the numbers in a list.
#Sample List : (8, 2, 3, -1, 7)
#Expected Output : -336

def mult(a):
    mul=1
    for i in a:
        mul=mul * i
    print(mul)

a=(8,2,3,-1,7)
mult(a)


#4. Write a Python program to reverse a string.
#Sample String : "1234abcd"
#Expected Output : "dcba4321"

def reverse_a_string(b):
    return b[::-1]    
b="1234abcd"
print("Reverse string : ", reverse_a_string("1234abcd"))


#5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

def factorial(c):
    if c==1 or c==0:
        return 1
    else:
        return (c*factorial(c-1))
c = int(input("entr the value : "))
result= factorial(c)
print("factorial of ", c,"is : ", result)

=======
# MAP Function():

def add_2(x):
    x+=2
    return x
num_list=[1,2,3,4,5,6]
print("original list is : ", num_list)
new_list=(list(map(add_2,num_list)))
print("modified list is : ", num_list)



# Reduce () Function:
from functools import reduce
def add(x,y):
    return x+y
num_list = [1,2,3,4,5]
print("sum of values in list = ")
print(reduce(add, num_list))

#filter () Function :
def check(x):
    if (x % 2 == 0 or x % 4 == 0):
        return 1
evens = list(filter(check,range(2,22)))
print(evens)



#1. Write a Python function to find the maximum of three numbers.

def max_of_three(a,b,c):
    return max(a,b,c)
a=20
b=39
c=32
operation = max_of_three
print(max_of_three(a,b,c))


#2. Write a Python function to sum all the numbers in a list.
#Sample List : (8, 2, 3, 0, 7)
#Expected Output : 20

def sum_of_numbers():
    total= sum_of_numbers
    return total
total=8,2,3,0,7
print(sum(total))

#3. Write a Python function to multiply all the numbers in a list.
#Sample List : (8, 2, 3, -1, 7)
#Expected Output : -336

def mult(a):
    mul=1
    for i in a:
        mul=mul * i
    print(mul)

a=(8,2,3,-1,7)
mult(a)


#4. Write a Python program to reverse a string.
#Sample String : "1234abcd"
#Expected Output : "dcba4321"

def reverse_a_string(b):
    return b[::-1]    
b="1234abcd"
print("Reverse string : ", reverse_a_string("1234abcd"))


#5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

def factorial(c):
    if c==1 or c==0:
        return 1
    else:
        return (c*factorial(c-1))
c = int(input("entr the value : "))
result= factorial(c)
print("factorial of ", c,"is : ", result)

>>>>>>> 283e1a9c18124363bd564a85dc529cae98ae0482
