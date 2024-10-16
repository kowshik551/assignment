'''
Tuple:- tuple is a collection of data types, it holds the group of values

1)tuple allow dupleycates.
2)typle is immutable object.
3)tuple insection order is preaseved.
4)tuple created by using tuple()function.
5)tuple allow index.

'''

#creating a tuple:
t=(1,2,True,5.345,"hari",3,2,4,4)
print(type(t))
print(len(t))

#creating a tuple using tuple() function:
t1=tuple(input("Enter the values: "))
print(t1)
print(type(t1))
print(len(t1))

#converting tuple items:
t2=input("Enter the values: ")
print(t2)
print(type(t2))
t2_1=tuple(t2)
print(t2_1)
print(type(t2_1))

#accessing tuple:
t3=tuple(input("Enter the value: "))
print(type(t3))
print(t3[2])
print(t3[-4])

#tuple slicing:
t4=("apple","banana","watermellon","cherry","mango","kiwi",1,2,3,4,5.43,"q","A","D","Q")
print(t4[0:])
print(t4[:-1])
print(t4[5:10])
print(t4[-13:-8])
print(t4[2:14:3])
print(t4[-13:-1:2])
print(t4[::-1])
print(t4[-1:])

#Tuple using operators:
t5=("apple","banana","watermellon","cherry","mango","kiwi")
if "cherry" in t5:
    print("yes, its exist")
else:
    print("not exist")


if "kowshik" in t5:
    print("yes, its exist")
else:
    print("not exist")

#chang the tuple vales:
t6=("apple","banana","watermellon","cherry","mango","kiwi",1,2,3,4,5.43,"q","A","D","Q")
print(t6)
print(type(t6))

t6_1=list(t6)
t6_1[10]="Ravi"
print(t6_1)
print(type(t6_1))

t6=tuple(t6_1)
print(t6,type(t6))

t6_2=list(t6)
t6_2.remove("Ravi")
print(t6_2)

t6=tuple(t6_2)
print(type(t6))


#packing and unpacking:
marks=36,48,59,70,80
print(marks,type(marks))





