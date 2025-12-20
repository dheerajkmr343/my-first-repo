# lst = []
# number = int(input("enter the number you want to store : "))
# for i in range (number):
#     element = input("enter the name of your choice ")
#     lst.append(element)
# print(lst)
# key = input("enter the name of you want to search for")
# for i in range (number):
#      if lst[i] == key:
#          print("element is ", lst[i])
#          print("element found")
#          break


# lst = []
# number = int(input("enter the number you want to store the name for : "))
# for i in range(number):
#     name = input("enter the name of your choice : ")
#     lst.append(name)
# print(lst)
# key = input("enter the name you want to search for : ")
# for i in range(number):
#     if key == number:
#         print("name found ", lst[i])
#         break





lst = []
number = int(input("How many number you want to store : "))
for i in range (number):
    num = int(input("enter the number you please : "))
    lst.append(num)
print(lst)    
key = int(input("please enter the number you want to search for : "))
for i in range (number):
    if lst[i]== key:  
        print("number found : ",lst[i])
        break