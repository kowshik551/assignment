#Write a program that forms a list of first character of every word in another list.
list_1=["hellow","wellcome","to","the","world","of","python"]
letters=[]
for word in list_1:
    letters.append(word[0])
print(letters)

#Write a program to create a list of numbers on the range 1 to 10 , then delete all odd numbers from the list and print the final list.

list_num=[]
for i in range(1,11):
    list_num.append(i)
print("original list: ", list_num)
for index, i in enumerate(list_num):
    if (i%2!=2):
        del list_num[index]
print("list after deletiong odd numbers: ", list_num)

#write a program to create a list of numbers in the specied range in particular steps.Reverse the list and print its values.
num_list=[]
m=int(input("Enter the starting of the range: "))
n=int(input("Enter the ending of the range: "))
o=int(input("Enter the step in the range: "))
for i in range(m,n,o):
    num_list.append(i)
print("Original list: ", num_list)
list_num.reverse()
print("Reversed list: ", num_list)

#write a program to create a list of fist 20 add numbers using the shortcut method.
odd=[2*i+1 for i in range(20)]
print(odd)

#Write a program to determine whether a person is eligible to vote or not . if he is not eligoble , display how many yers left to be eligible.
age=int(input("Enterthe age: "))
if(age>=18):
    print("your eligible to vote: ")
else:
    yers=18-age
    print("your have to wait for another" +" "+str(yers) + "yesrs to cast your vote")

#write a program to find larger of two numbers.
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
if(a>b):
    large=a
else:
    large=b
print("large=",large)




























































