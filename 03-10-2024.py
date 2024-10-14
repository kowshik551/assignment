'''#probleam 1)

s=input("Enter a word or sentence: ")
l=list(s.split())
print(l, type(l))
print(l[::-1])

print('---------------------------------------------------------------')

# probleam 2)

s1= input("Enter a word or sentence: ")
print(s1[::-1])

print('-------------------------------------------------------------------')

#probleam 3)

s2 =input("Enter a word or sentence: ")
print(s2.replace(" ",""))


print('-----------------------------------------------------------')

#probleam 4)

str=input("Enter a word or sentence: ")
l=list(str)
#print(l)
freq=[l.count(ele) for ele in l]
#print(freq)
d= dict(zip(l,freq))
print(d)

s= "hello"
s1= "karimulla"

print(s+" "+s1)

#output:-hello karimulla

s= "hello karimulla"
s1= "welcome to python programming"
print(s+"."+s1)


str="hello, "
x=input("\n Enter the name: ")
str += x
str += ". welcome to python programming"
print(str)

#output:-
# enter the name : kowshik
# hello kowshik.wellcome to python programmig
'''
'''write a program to print the following pattern?
A
AB
ABC
ABCD
ABCDE
ABCDEF

for i in range(1,7):
    ch='A'
    print()
    for j in range(1,i+1):
        print(ch, end=" ")
        ch=chr(ord(ch)+1)

    
for i in range(1,8):
    ch='B'
    print()
    for j in range(1,i+1):
        print(ch, end=' ')
        ch=chr(ord(ch)+1)
'''

message=input("Enter the massage: ")
index=0
for i in message:
    print("message[", index,"]= ", i)
index += 1












































































































































