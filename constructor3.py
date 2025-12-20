class company:
  def __init__(self):
    self.fname = input("enter your fname ---> ")
    self.lname = input("enter your lname ---> ")
    self.designation = input("enter your designation ---> ")

  def printdata(self):
    print(f"hello my firstname is {self.fname} and last name is {self.lname} and my desingation is {self.designation}")



class employee(company):
  def __init__(self):
    # company.__init__(self)
    super().__init__()
    self.employee_id = input("enter your employee id ---> ")
    self.company_name = input("enter your company name ---> ")

  def printdata(self):
    # company.printdata(self)
    super().printdata()
    print(f"my employee id is {self.employee_id} and my company name is {self.company_name}")


a = employee()
a.printdata()    
