print("We will calculate how much time do you still have in life \n but is just a joke")

age = int(input("How old are you: "))

years_left = 90 - age

months = (years_left * 12)

weeks = (years_left * 52)

days = (years_left * 365)

print("You still have " + " " + str(months) + " " + "months")
print("or")
print(f"You still have {weeks} weeks")
print("or")
print(f"You still have {days} days")
print("in your life, so take it seriously")
