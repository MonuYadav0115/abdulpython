# check the leap year or not

year = int(input("Enter the year"))
if year % 100 ==0:
    if year % 400 ==0:
        print("leap year")
    else:
        print("Not a leap year")
elif year % 4 ==0:
    print("leap year")
else:
    print("not a leap year")
