# lst = ["Dheeraj", "Neeraj", "Mitali", "Ishika", "Arav"]
# # print(type(lst))

# # mylst = dict(lst)
# # print(type(mylst))

dct1 = {"fname":"Ritesh", "lname":"Kumar"}
del dct1["lname"]
print(dct1)



dct2 = {"name": "Dheeraj", "Address": "New Delhi", "Company" : "TCS"}
myadd = dct2.pop("Address")
print(myadd)
print(dct2)