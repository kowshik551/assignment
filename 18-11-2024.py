# ENCAPSULATION : The process of grouping/bunding data along with method.


class Employee:
    def __init__(self):
        self._employee_id = int(input("Employee Id Here : "))
        self.name = input("Enter Employee Name : ")
        self.__salary = int(input("Enter Employee Salary : "))
        self.address = input("Enter Employee Address : ")
 
    def get_employee_details(self):
        print("Employee Id : ",self._employee_id)
        print("Employee Name : ",self.name)
        print("salary : ",self.__salary)
        print("Address : ",self.address)
 
    def update_address(self):
        self.new_address = input("Enter Emplotee New Address Here : ")
    def update_details(self):
        print("New Address : ",self.new_address)

        if self.address == self.new_address:
            print(f"{self.address}")
        elif self.address != self.new_address:
            print(f"{self.new_address}")
        else: 
            print("NA")

    def __validate_employee_ID(self):
        self._employee_id == self._employee_id
        pass

e=Employee()
e.get_employee_details()
e.update_address()
e.update_details()


class bank_account:
    def __init__(self):
        self.__acc_num = int(input("Enter Account Number Here : "))
        self.__pin_num = int(input("Enter PIN NUmber Here : "))
        self.__amount = int(input("Enter Deposite Amount Here : "))
        self.__pin = 2345
    def bank_deteils(self):
        print("Account Number : ",self.__acc_num)
        print("PIN Number : ",self.__pin_num)
        
        print("pin : ",self.__pin)
    def deposite(self):
        if self.__pin == self.__pin_num:
            print("Deposite Amount : ",self.__amount)
            self.balance = 0
            self.balance += self.__amount
            print("Total Balance : ",self.balance)
        else:
            print("invalid pin number")

    def withdraw(self):
        if self.__pin != self.__pin_num:
            self.__withdraw = int(input("Enter Withdraw Amount Here : "))
            if self.__withdraw <= self.balance:
                self.balance -= self.__withdraw
                print("Total Balance : ",self.balance)
            else:
                print("Insufficient funds")
        else:
            print("invalide pin number")
        
 
    def check_balance(self):
        print(self.balance)
 
    def _validate_PIN(self):
        if self.__pin == self.__pin_num:
            print("courrect")
        else:
            print("Invalid PIN")
        

c=bank_account()
c.bank_deteils()
#c._validate_PIN()
c.deposite()
c.withdraw()
c.check_balance()

