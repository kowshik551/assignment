'''# !)Write a program that counts the number of even and odd numbers in a list.
numbers=[1,2,3,4,5,6,7,8,9,10]
even_count=0
add_count=0
for number in numbers:
    if number%2==0:
        even_count +=1
    else:
        add_count +=1
print("number of even numbers: ",even_count)
print("number of add numbers: ",add_count)

print('-----------------------------------------------------------------')

# 2)Write a program that prints the multiplication table for a given number.

n=int(input("Enter the value: "))
print("multiplication table of: ",n)
for i in range(1,11):
    print(n,'x',i,'=',n*i)

print('------------------------------------------------------------------')

# 3)Write a program to find the largest of three numbers using if statements.

number1=float(input("Enter The First Number: "))
number2=float(input("Enter The Second Number: "))
number3=float(input("Enter The third Number: "))
largest = number1
if number2>largest:
    largest= number2
if number3>largest:
    largest= number3
print("The Largest Number: ", largest)

# 4)Write a program to calculate the factorial of a number using a for loop.

n=int(input("enter the value: "))
factorial=1
for i in range(1, n+1):
    factorial *=i
print(f"the factorial of{n} is {factorial}")

# 5)Write a program that takes a number as input and prints the sum of its digits. 

number=input("Enter the value: ")
sum_of_digit=0
for digit in number:
    sum_of_digit += int(digit)
print("the sum of digits is: ",sum_of_digit)

# 6)Write a program that generates a random number between 1 and 100, and asks the user to guess it. The program should give hints ("too high" or "too low") until the user guesses correctly.

n = int(input("my gussing number is: "))
guess = None  
print("selecte the guess in number between 1 to 100")
while guess != n:
    guess = int(input("Guess a number:"))
    if guess<1 and guess>100:
        print(" guess a number between 1 and 100.")
    elif guess > n:
        print("Too high!")
    elif guess < n:
        print("Too low!")
    else:
        print("Correct!")

# 7)write a program to check if a number is an Armstrong number
n =int(input("enter a number:"))
temp=n
1==len(str(n))
sum=0
while(temp):
    r=temp%10
    sum=sum+r**1
    temp=temp//10
    print(sum)
if(sum==n):
    print("is a armstrong Number")
else:
    print("is not an Armstrong number")

# 8)write a program to check if a string is a palindrome.
n=int(input("Enter a value: "))
temp=n
sum=0
while(n):
    r=n%10
    sum=sum*10+r
    n=n//10
print(sum)
print(n)
if(sum==temp):
    print("is a polindrome")
else:
    print("is not a polindrome")

# 9)write a program that check if a number is prime.

num =int(input("enter a number: "))
if num==1:
    print("not a prime number")
    if num>1:
        for n in range(2,num):
            if num%2==0:
                print(num, "is not a prime number ")
                break
            else:
                print(num, "num is a prime number")
'''
# 10)Write a program that prints the numbers from 1 to 100. 
#For multiples of three, print "Fizz" instead of the number, and for multiples of five, print "Buzz". 
#For numbers which are multiples of both three and five, print "FizzBuzz".
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)




