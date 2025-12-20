students = int(input("enter the number of passing students :"))
if students > 100 :
    print("more than 100 students are passing")
    if students > 200:
        print("more than 200 students are passing ")
        if students > 300:
            print("more than 300 students are passing ")
        else:
            print("More than 300 students are passing ")
    else:
        print("More 200 students are passing but less than 300")
else:
    print("Students less than 100 are passing ")                    