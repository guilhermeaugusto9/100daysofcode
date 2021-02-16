print("Hello and welcome to the pizza planet !")

size = input("What size of pizza do you want ? (S,M,L)")
bill = 0

if size == 'S':
    bill = 15
    pp = input("do you want peperoni? (Y,N)")
    if pp == "Y":
        bill += 2
    else:
        bill = 15
elif size == "M":
    bill = 20
    pp = input("do you want peperoni? (Y,N)")
    if pp == "Y":
        bill += 3
    else:
        bill = 20
elif size == "L":
    bill = 25
    pp = input("do you want peperoni? (Y,N)")
    if pp == "Y":
        bill += 3
    else:
        bill = 25
cheese = input("do you want extra cheese (Y,N) ?")
if cheese == "Y":
    bill += 1
    print(f"thank you for your order the price is ${bill}")
else:
    print(f"thank you for your order the price is ${bill}")

# print(f"thank you for your order the price is ${bill}")
