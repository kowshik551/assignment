'''
Executive summary:
The document discusses about python operators  and Data Types
Operators:
Operators are used to perform operations on variables and values.
Various operators supported by Python are:
1.Arithmetic operators
2.Comparision operators
3.Logical operators
4.Assignment operators
5.Identity operators
6.Membership operators
7.Bitwise operators

1.Arithmetic operators: for performing Arithmetic operations.
Various Arithmetic operators are:
1.Addition(+) :- adds two operands.
2.Subtraction(-) :- subtracts two operands.
3.Multiplication(*) :- multiplies two operands.
4.Division(/) :- divides the first operand by the second.
5.Floor Division(//) :- divides the first operand by the second.
6.Modulo Division(%) :- returns the remainder when the first operand is divided by the second.
7.Exponent(**) :- Returns first raised to power second.
Ex:-
x=10
y=4
add=x+y
print("sum=",add)
sub=x-y
print("diff=",sub)
mul=x*y
print("product=",mul)
div=x/y
print("Division=",div)
Output:-
sum= 14
diff= 6
product= 40
Division= 2.5
Ex:-
floordiv=x//y
print("Floordivision=",floordiv)
moddiv=x%y
print("moddiv=",moddiv)
exp=x**y
print("exp=",exp)
Output:-
Floordivision= 2
moddiv= 2
exp= 10000

2.Comparision operators:- Comparison operators are used to compare two values. Comparison operators always returns either True/False
== :- True if both operands are equal.
!= :- True if operands are not equal.
>= :- Greater than or equal to True if the left operand is greater than or equal to the right.
<= :- Less than or equal to True if the left operand is less than or equal to the right.
> :- True if the left operand is greater than the right.
< :- True if the left operand is less than the right.
Ex:-
x=10
y=4
print(x>y)
print(x<y)
print(x>=y)
Output:-
True
False
True
Ex:-
x = 5
y = 3
print(x <= y)
print(x > y)
print(x < y)
Output:-
False
True
False
3.Logical operators:- Logical operators are used to combine conditional statements.
AND :- True if both the operands are true.
OR :- True if either of the operands is true.
NOT :- True if the operand is false.
Ex:-
x = 5
print(x > 3 and x < 10)
Output:-
True
Ex:-
x = 9
print(x > 3 or x < 4)
print(not(x > 3 and x < 10))
Output:-
True
False
4.Assignment operators:- Assignment operators are used to assign values to variables. Assignment operators are also called as short-hand operators.
= :- Assign the value of the right side of the expression to the left side operand.
+= :- Add right-side operand with left-side operand and then assign to left operand.
-= :- Subtract right operand from left operand and then assign to left operand.
*= :- Multiply right operand with left operand and then assign to left operand.
/= :- Divide left operand with right operand and then assign to left operand.
%= :- Takes modulus using left and right operands and assign the result to left operand.
//= :- Divide left operand with right operand and then assign the value(floor) to left operand.
**= :- Calculate exponent(raise power) value using operands and assign value to left operand.
&= :- AND on operands and assign value to left operand.
|= :- OR on operands and assign value to left operand.
^= :- XOR on operands and assign value to left operand.
>>= :- Performs Bitwise right shift on operands and assign value to left operand.
<<= :- Performs Bitwise left shift on operands and assign value to left operand.
Ex:-
x = 5
x += 3
x -= 3
x *= 3
x /= 3
x%=3
print(x)
print(x)
print(x)
print(x)
print(x)
print(x)
Output:-
5
8
2
15
1.6666667
2
Ex:-
x = 10
x//=6
x **= 6
x &= 6
x |= 6
x ^= 6
x >>= 6
x <<= 6
print(x)
print(x)
print(x)
print(x)
print(x)
print(x)
print(x)
Output:-
1
1000000
2
14
12
0
640

5.Identity operators :- These operators are used to compare the addresses of 2 objects.
Identity operators are,
  Is :- Returns True if both variables are the same object.
  is not :- Returns True if both variables are not the same object.
Ex:-
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z) 	# returns True because z is the same object as x.
print(x is y)	# returns False because x is not the same object as y, even if they have the same content.

output:-
True 
False
True
Ex:-
x = ["car", "bus"]
y = ["car", "bus"]
z = x
print(x is not z)
print(x is not y)

output:-
False
True

6.Membership operators:- These operators are used to check whether an element is present or not.
Membership operators are:
  In :- Returns True if a sequence with the specified value is present in the object.
  not in :- Returns True if a sequence with the specified value is not present in the object.
Ex:-
x = ["apple", "banana"]
print("banana" in x)

output:-
True
Ex:-
x = ["kowshik", "ajay"]
print("veeru" not in x)

output:-
true

7.Bitwise operators:- Bitwise operators are used to compare (binary) numbers.
AND (&) :- Sets each bit to 1 if both bits are 1.
OR ( | ) :- Sets each bit to 1 if one of two bits is 1.
XOR( ^ ) :- Sets each bit to 1 if only one of two bits is 1.
NOT ( ~ ) :- Inverts all the bits.
LIFT SHIFT ( << ) :- Shift left by pushing zeros in from the right and let the leftmost bits fall off.
RIGHT SHIFT ( >> ) :- Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost 
bits fall off.
Ex:-
Print(6 & 3)
Print(6 | 3)
Print(6 ^ 3)
Output:-
2
7
5

Ex:-
Print( ~5)
print(3 << 2)
print(8 >> 2)
Output:-
-6
12
2

Data types:-
Date typer are two types
Fundamental data types
Collection data types

Fundamental data types:-
i)int :- A python int() function convert the specified value into an integer number.
Ex:-
A=5
Print(type(a))
Output: -
< class ‘int >

ii)float :- The float data type represents a floating point or decimal number.
Ex:-
A=5.0
Print(type(a))
Output: -
< class ‘float’ >

iii)complex :- The complex data type in python consists of two values , the first one is the real part of the
		complex number, and the second one is the imaginary part of the complex number.
Ex:-
Ex: -
(3+7j)

iv) Boolean:- Python Boolean type is one of the bult-in data types provided by python .which represents
		one of the two value  i.e., true (or) false. 
Ex:-
X=200
Y=33
Print b>a
Output: -
False

v) String data type:- A string is a collection of one or more characters put in a single quotes , double quotes, and triple quotes. It is represented by “str” .the string is immutable, so its values cannot be changed.

String methods:-

Capitalize:- Converts the first character to upper case.
Ex: -
x = "india"
print(x.capitalize())
output:-
India

Title():- For capitalizing the 1st character of each word in a string
Ex:-
x = "India is my country"
print(x.title())
output:-
India Is My Country

Collection data types:-
List:- List is a collection data type which holds grope of values.
List properties
List represented by using [ ]
List allows both homogeneous (similar) and heterogenous(dissimilar) elements.
Ex: -X=[10,20,30,40,50] homogeneous elements
        Y=[101,’kowshik’,30369,40,true] heterogenous elements
List allows duplicates 
Ex: - X= [10,20,30,40,50,10,20,30]
In section order is followed i.e., the order in which the elements are inserted in the same order they are stored or displayed
Ex: - X=[10,20,30,40,50]
Each element of list is identified or accessed by a unique index
List supports 2 types of indexes:
Positive index (or) Forword index
Negative index (or) backword index
Ex: - 
O	     1	       2	          3		4	5 --- positive (or) Forword index
P	Y	T	H	O	N
                                                                                           
		
			-6	   -5           -4             -3            -2            -1  -- negative (or) backword index
Change the item value:-
To change the value of a specific item, refer to the index number:
Ex: -
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) 
Output:-
[‘apple’,’blackcurrant’,’cherry’]

List methods :-

Append :- adds an element at the end of the list
Ex: -
thislist = ["apple", "banana", "cherry"]
thislist. append("orange")
print(thislist)
Output:-
[‘apple’, ’banana’, ’cherry’, ’orange’]

TUPLE :- Tuple is a collection datatype which holds group of values.
Tuples are used to store multiple items in a single variable.
A tuple is an immutable object, which means it cannot be changed, and we use it to represent fixed collections of items.
Tuple is allowing duplicate values
Ex: - x=(10,20,30,40)
Elements of tuples are enclosed in parenthesis ( ) round brackets and are separated by commas.
Like list and string, elements of a tuple can be using index values.

 0  1   2   3   4   5  --- positive (or) Forword index
 P  Y   T   H   O   N                                                                                               
-6 -5  -4  -3  -2  -1  -- negative (or) backword index

Tuple = ( )						#empty tuple
Tuple = (1)						#tuple with single element
Tuple1 = (1,2,3,4,5)					#tuple of integers
Tuple2 = (“economics”,87,”accountancy”, 89.9)	#tuple of mixed data types
Tuple is an immutable object i.e.; changes and modifications are not allowed within a tuple but elements of a tuple can be either mutable or immutable
 ex: y=(101,"James",70890.70,[1,2,3])
 tuple can also be created by using tuple() function.
Tuple allows both homogenous(same datatype) and heterogeneous(different datatype) elements
ex:  x=(10,20,30,40,50)  			#homogenous elements
       y=(101,"James",70890.70,[1,2,3]) 	#heterogeneous elements
NOTE: - If there is only one element within a tuple then it is not tuple.: -
Ex: -
x = (10,20,30,40,50)
print(x)
Print(type(x))
Print(id(x))
Output:-
(10,20,30,40,50)

Ex:-
thistuple = ("apple","banana","cherry")
print(thistuple[1])
output: -
banana 

SET :- Set is a collection datatype which holds group of values.
Set represented by using curly braces{ }.
Set allows homogeneous & heterogeneous elements.
Set allows duplicates.
In set order is not preserved.
Set doesn't support indexing. 
Set cannot access using while loop and index.
Set can access the elements of a set using for loop.
Set is a mutable object , but elements of set should be immutable only.
Set can be created directly by allowed by using { } or by using set( )function.
Set within  a set is not allowed because set  set allowed only immutable within it.
We can perform mathematical operation on a set object.  

Ex:-
thisset = {"apple","banana","cherry"}
print(thisset)
output: -
{'banana', 'apple', 'cheery'}

Ex:-
thisset = set("hello")
print(thisset)
output: -
{'e', 'a', 'p', 'l'}

DICTIONARY :- Dictionary is a collection data type which holds group of (key, values)
Ex: -
thisdict ={"brand":"Ford","model":"Mustang","year":1964}
print(thisdict)
Output: -
{''brad': 'ford', 'model':'mustang', 'year': 1964}
     KEY	         VALUES          K		  V		K	     V
Properties of a dictionary: -
Dictionary represented by using curly braces { }.
Keys and values can be either homogeneous or heterogeneous.
Keys cannot be duplicated, but values can be duplicated
Ex: -
Age=60  wight=60
Insertion order is not preserved.
Indexing/slicing is not supported
Dictionary is mutable object. Within a dictionary , we can both mutable and immutable types.
Dictionary can be created directly by using { } or by using dict( ) function.
To access a elements of a dictionary , if we pass the key, we will get the value
Ex: -
X[“age]-returns value 25

Ex:- 
Print the “brand” value of the dictionary:
thisdict ={"brand":"Ford", "model":"Mustang", "year":1964}
print(thisdict["brand"])
Output: -
Ford

Ex:-
thisdict ={"brand":"Ford", "model":"Mustang", "year":1964}
thisdict["year"] =2018
print(thisdict)
Output:-
{"brand":"Ford", "model":"Mustang", "year":2018}

'''

