#probleam 1)

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