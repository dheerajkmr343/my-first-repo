studentsname = ["Vikas", "Dheeraj", "Neeraj", "Ishika", "Mitali", "Prateek"]
print(studentsname[1])
print(studentsname.index("Ishika"))
studentsname[4] = "Ishu"
print(studentsname)

c= ("Vikas", "Dheeraj", "Neeraj", "Ishika", "Mitali", "Prateek")
print(type(c))
print(c[4])
c = list(c) 
print(type(c))
c[4] = "Ammu"
print(c)