#7. Nested Lists:
#1.Write a Python program to create a 3x3 matrix (nested list) and print the matrix. Then, access and print the element at row 2, column 3.
nl=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(nl)):
    print(nl[i])
element=nl[1][2]
print(element)

#2.Create a nested list representing a list of students' names and their respective grades. Write a Python program to print each student's name along with their grade.
nl2=[["kowshik","A+"],["ajay","A"],["hari","B+"],["venkat","B"],["siva","C"]]

for p,q in nl2:
    print("Name: ",p)
    print("Grade: ",q)
