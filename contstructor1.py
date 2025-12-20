class company:
  def __init__(self):
    self.fname = input("enter your first name ---> ")
    self.lname = input("enter your last name ---> ")
    self.address = input("enter your addresss ---> ")

  def printdata(self):
      print(f"employee details are {self.fname, self.lname, self.address }")

class employee:
  def __init__(self):
    company. __init__(self)
    self.employee_id = input("enter your employee id ---> ")    

  def printdata(self):
    print(f"person employee id is {self.employee_id}")
    company.printdata(self)


ob1 = employee()
ob1.printdata()
    


  


# class class22:
#   def __init__(self):
#     self.fname = input("enter your first name --> ")
#     self.lname = input("enter your last name --> ")
#     self.address = input("enter your address  --> ")

# class student(class22):
#   pass    


# obj1= student()