print("Lets test if a year is a leap year")

year = float(input("Type a year bro: "))


test1 = int(year % 4)
test2 = int(year % 100)
test3 = int(year % 400)

if test1 > 0:
    if test2 > 0:
        if test3 > 0:
            print("not a leap year")
        else:
            print("is a leap year")
    else:
        print("not a leap year")
else:
    print("not a leap year")
