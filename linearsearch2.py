# lst = [1,2,3,4,5,6,7,8,9]
# for i in range(len(lst)):
#     print("hello ", lst[i])
#     if lst[i] == 5:
#         print("found the number : ")
#         break


# # # lst = ["p1", "p2", "p3", "p4", "p5", "p6", "p7"]
# # # for i in range(len(lst)):
# # #     if lst[i] == "p3":
# # #         continue
# # #     print("Hello ", lst[i])


# lst1 = ["Dheeraj", "Mahima", "Priya"]
# lst2 = ["Neeraj", "Rupesh", "Pranjal"]
# for i in  lst1:
#     for j in lst2:
#         print(i,j)



# i = 0
# while i < 5:
#     print("hello")
#     i = i + 1


starting = int(input("enter starting number --> "))
ending = int(input("enter ending number --> "))
while  starting < ending :
    if starting % 2 == 0:
        print(f"{starting} is an even number ")
    else:
        print(f"{starting} is an odd  number ")
    starting = starting + 1 
