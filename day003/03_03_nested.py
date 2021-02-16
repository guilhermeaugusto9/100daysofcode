print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


if height >= 120:
    print("you can ride the rolercoaster !")
    age = int(input("How old are you?"))
    if age <= 12:
        print("Please pay S5")
    elif age <=18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry, you need to grow before you can ride!")
