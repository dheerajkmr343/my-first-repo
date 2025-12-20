# class student:
#   def __init__(self, f_name, l_name):
#     print("inside the constructor")
#     self.f_name = f_name
#     self.l_name = l_name

# obj1 = student("Dheeraj", "Kumar")
# obj2 = student("Neeraj", "Kumar")
# print(f"My first object details are {obj1.f_name} {obj1.l_name} and second object details is {obj2.f_name} {obj2.l_name}") 



# class employee:
#   def __init__(self, fname,lname):
#     print("calling the constructor")
#     self.fname = fname
#     self.lname = lname

#   def printfunction(self):
#     print(f"my name is {self.fname} and my last name {self.lname}")

#   def samplefunction(self):
#     print(f"my name is {self.fname} and my last name {self.lname}")



# testing = employee("Dheeraj", "Kumar")
# testing.samplefunction()



class student:
  fname = "unknow"
  lname = "unknow"
  school = "unknown"

obj1 = student()
print(f"my first name {obj1.fname} and last name {obj1.lname} and school name {obj1.school}")

obj1.fname = "Dheeraj"
obj1.lname = "Kumar"
obj1.school = "GBSSS"

print(f"my first name {obj1.fname} and last name {obj1.lname} and school name {obj1.school}")

del obj1.school
print(f"my first name {obj1.fname} and last name {obj1.lname} and school name {obj1.school}")







