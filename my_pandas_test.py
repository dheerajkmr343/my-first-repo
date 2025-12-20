import pandas as pd
# dct = {"Name":["Dheeraj", "Pankaj", "Sharad"], "Place": ["Delhi", "Mumbai","Kolkata"]}
# data = pd.DataFrame(dct)
# print(data)


# num = int(input("How many names you want to store : "))
# namelst = []
# placelst = []
# for i in range(num):
#   name = input("Enter the name : ")
#   place = input("Enter the place : ")
#   namelst.append(name)
#   placelst.append(place)
#   ("\n")
# dct = {"name": namelst, "place": placelst}  
# data = pd.DataFrame(dct)
# print(data)





# num = int(input("How many names you want to store : "))
# namelst = []
# placelst = []
# occupationlst = []
# for i in range(num):
#   name = input("Enter the name : ")
#   place = input("Enter the place : ")
#   occupation = input("Enter the occupation : ")
#   namelst.append(name)
#   placelst.append(place)
#   occupationlst.append(occupation)

#   ("\n")
# dct = {"name": namelst, "place": placelst, "occupation": occupationlst}  
# data = pd.DataFrame(dct)
# print(data)



num = int(input("How many students you have : "))
namelst = []
classlst = []
sectionlst = []
for i in range(num):
  name = input("enter the name of the student: ")
  classA = int(input("which class do they belong to: "))
  section = input("enter the section: ")
  namelst.append(name)
  classlst.append(classA)
  sectionlst.append(section)
dct = {"Names" : namelst, "Classes": classlst, "Section": sectionlst }
data = pd.DataFrame(dct)
print(data)
