# Instance Method:- Instance methods can access all attributes of the instance and have self as a parameter.

#Ex:-

class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

    # instance method to access instance variable
    def show(self):
        print('Name:', self.name, 'Age:', self.age)

# create first object
print('First Student')
emma = Student("ravi", 14)
# call instance method
emma.show()

# create second object
print('Second Student')
kelly = Student("hari", 16)
# call instance method
kelly.show()


# @classmethod:- To create a class method, we use the @classmethod decorator or the classmethod()
#                function. The method should take cls as its first parameter, which refers to the class itself.

# Ex:-

class School:
    # class variable
    name = 'chithanya School'

    def school_name(cls):
        print('School Name is :', cls.name)

# create class method
School.school_name = classmethod(School.school_name)

# call class method
School.school_name()


#Ex:-

class Student:
    school_name = 'narayana School'

    def __init__(self, name, rool_no):
        self.name = name
        self.roll_no = rool_no

    @classmethod
    def change_school(cls, school_name):
        # class_name.class_variable
        cls.school_name = school_name

    # instance method
    def show(self):
        print(self.name, self.roll_no, 'School:', Student.school_name)

jessa = Student('Jessa', 20)
jessa.show()

# change school_name
Student.change_school('prathibha School')
jessa.show()


# Static method:- static method does not require an instance of the class to be called and cannot access
#                 or modify the class state.


# Ex:-
class employee:
    @staticmethod
    def sample(x):
        print("Inside static method", x)

employee.sample(10)
emp = employee()
emp.sample(10)



# Ex:-

class auth:
    @staticmethod
    def validate_password(password):
        if len(password) <6:
            return False
        else:
            return True
        
is_valid = auth.validate_password("welcome123")
print("password is valid : ", is_valid)