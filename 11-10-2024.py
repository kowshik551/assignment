# make list of five random numbers.

list_ran=list(range(1,50,5)) 
random_num=[]
for i in list_ran:
    random_num.append(i)
print(random_num)

#Make a list of first ten letters of the alphabet,then using the slice operation di the following operation
#print the first three lrtters fromthe list.
# print any three lettersfrom middle.
# print the letters from any particular index to the end of the list.
list=['a','b','c','d','e','f','g','h','i']
print(list)
print(list[:3])
print(list[2:7])
print(list[-1])

#Write a program the defines a list of countries that are a member of BRICS. Check whether a country is a members of BRICS or not.
country=["Brazil","India","China","Russia","Sri Lanka"]
is_country=input("Enter the name of country: ")
if is_country in country:
    print(is_country, "has also joined BRICS")
else:
    print(is_country, "has not joined BRICS")

#Write a program to create a list of numbers in the range1 to 10. Then delete all even numbers form the list and print the final list.
list_num=[]
for i in range(1,11):
    list_num.append(i)
print("Original list: ", list_num)
for index, i in enumerate(list_num):
    if (i%2==0):
        del list_num[index]
print("List After Deleting Even Numbers : ", list_num)

#Write a function that takes a list as input and returns a new list with the elements in reverse order.
list_num=[1,4,3,5,2,6,8,10]
list_num.reverse()
print(list_num)
    
#Write a program that finds the maximum number in a list without using built-in functions.
lm=[1,2,3,4,5,6,10,30,200,15,35,46,32,12,27,0,66]
lm2=max(lm)
print(lm2)

#Given a list, write a function that counts how many times a specific element appears in the list.
lm_2=["apple","banana","apple","kiwi","orange","cherry","apple"]
lm_12=lm_2.count("apple")
print(lm_12)


















































