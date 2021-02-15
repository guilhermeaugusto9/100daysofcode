# greeting

print("Welcome to the tip calculator we will help you to calculate how much every person will gonna pay")

# first variable

total = input("What is the totall bill ? (use the this format ex: R$120):  ")

# split to just get the number

total_num = float(total.split("R$")[1])

# get the divider

persons = float(input("How many persons will divide the bill? : "))

# get the tip

tip = float(input("what percentage of tip do you like to give>? 10 , 12 or 15 ? "))

# get the tip mulitplier

tip_multiplier = tip / 100

final_value = round(float((total_num * tip_multiplier + total_num) / persons), 2)

# print the result

print(f"Each person should pay: \n R$ {final_value}")

