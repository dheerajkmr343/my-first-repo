# class father:
#   def __init__(self):
#     self.fname = input("enter your first name ---> ")
#     self.lname = input("enter your last name ---> ")
#     self.sname = input("enter your sur name ---> ")

#   def printdata(self):
#     print(f"my son's demographic details are {self.fname, self.lname, self.sname}")

    
# class son:
#   def __init__(self):
#     father. __init__(self)
#     self.address = input("enter your address --->")
#   def printdata(self):
#     print(f"son's address details is {self.address}")
#     father.printdata(self)


# obj1 = son()
# obj1.printdata()


class car:
  def __init__(self):
    self.make = "swift"
    self.model = "VDI"
    self.year = "2024"

Car = car()
print(Car.make, Car.model, Car.year )



class Bike:
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year

bike = Bike("Pulsar", "2025", "2025")
print(bike.make,bike.model, bike.year)







class Employee:
  def __init__(self, name, emp_id, designation):
    self.name = name
    self.emp_id = emp_id
    self.designation = designation
employee = Employee("Dheeraj", "1977050", "DevOps Engineer")
print(employee.name, employee.emp_id, employee.designation)    
    

    