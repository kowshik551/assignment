# Dictionary:
# Dictionary representd by using {}.
# Keys can not duplicated, but Values can be duplicated.
# Dictionary is a mutable object.
# Dictionary can be created directly by using dict() function.
# To access a elements of a dictionary, we pass the key we will get 

# Create a dictionary :
dict_1={}
key=(input("Enter key here : "))
value=(input("Enter value here : "))
dict_1[key]=value
print(dict_1)
#               (or)
for iteam in range(3):
    key=(input("Enter key here : "))
    value=(input("Enter value here : "))
    dict[key]=value
print(dict)

dict_2={"Kohli":90,"Rohit":65,"Gill":35,"Suryakumar":50,"Bumrah":30,"Rahul":100,"Shreyes":70,"Siraj":25,"Kihan":60,"Shami":20,"Ashwin":25}
print(dict_2)
print(type(dict_2))
print(len(dict_2))

# Accessing the values of a dictionary
dict_3={"Kohli":90,"Rohit":65,"Gill":35,"Suryakumar":50,"Bumrah":30,"Rahul":100,"Shreyes":70,"Siraj":25,"Kihan":60,"Shami":20,"Ashwin":25}
print(dict_3["Kohli"])
print(dict_3["Ashwin"])
print(dict_3["Siraj"])

# Get keys :
dict4_1={"Kohli":90,"Rohit":65,"Gill":35,"Suryakumar":50,"Bumrah":30,"Rahul":100,"Shreyes":70,"Siraj":25,"Kihan":60,"Shami":20,"Ashwin":25}
dict4=dict4_1.keys()
print(dict4)

# Get Values :
dict5_1={"Kohli":90,"Rohit":65,"Gill":35,"Suryakumar":50,"Bumrah":30,"Rahul":100,"Shreyes":70,"Siraj":25,"Kihan":60,"Shami":20,"Ashwin":25}
dict5=dict5_1.values()
print(dict5)

# Check if Key Exist :
dict6={"Kohli":90,"Rohit":65,"Gill":35,"Suryakumar":50,"Bumrah":30,"Rahul":100,"Shreyes":70,"Siraj":25,"Kihan":60,"Shami":20,"Ashwin":25}
if "Bumrah" in dict6:
    print("yes, he exist")

# Chaing dictionary items :

dict7={"Kohli":90,"Rohit":65,"Gill":35,"Suryakumar":50,"Bumrah":30,"Rahul":100,"Shreyes":70,"Siraj":25,"Kihan":60,"Shami":20,"Ashwin":25}
dict7["Kohli"]=150
print(dict7)

# update dictionary :

dict8={"Kohli":90,"Rohit":65,"Gill":35,"Suryakumar":50,"Bumrah":30,"Rahul":100,"Shreyes":70,"Siraj":25,"Kihan":60,"Shami":20,"Ashwin":25}
dict8.update({"Jadeja":100})
print(dict8)
print(len(dict8))

# Removing dictionary items:
dict9={"Kohli":90,"Rohit":65,"Gill":35,"Suryakumar":50,"Bumrah":30,"Rahul":100,"Shreyes":70,"Siraj":25,"Kihan":60,"Shami":20,"Ashwin":25}
print(len(dict9))
dict9.pop("Rahul")
print(dict9)
print(len(dict9))
#                       (or)
dict10={"Kohli":90,"Rohit":65,"Gill":35,"Suryakumar":50,"Bumrah":30,"Rahul":100,"Shreyes":70,"Siraj":25,"Kihan":60,"Shami":20,"Ashwin":25}
print(len(dict10))
del dict10["Bumrah"]
print(dict10)
print(len(dict10))
#                       (or)
dict11=dict10
print(dict11)
dict11.popitem()
print(dict11)

# program to create 10 key-value pairs where key is a numberd= in the range 1-10 and the value is twice the number.
dict_12={x :2*x for x in range(1,11)}
print(dict_12)

