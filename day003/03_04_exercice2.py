# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = float(round((weight/(height**2)),2))

print("Your BMI is equals to: " + "\n" + str(BMI))

if BMI < 18.5:
    print(f"Your BMI is equals to {BMI}, you are classified as Underweight")
elif BMI < 25:
    print(f"Your BMI is equals to {BMI}, you are classified as normal")
elif 25.00 <= BMI <= 30.00:
    print(f"Your BMI is equals to {BMI}, you are classified as overweight")
elif 30.00 < BMI <= 35.00:
    print(f"Your BMI is equals to {BMI}, you are classified as obese")
elif BMI > 35.00:
    print(f"Your BMI is equals to {BMI}, you are classified as superobease go to a doctor")
else:
    print("the calculator is failed")


