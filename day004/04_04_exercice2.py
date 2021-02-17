# this program will ramdomic chose whos gona pay everybody bill

import random

print("Welcome to the russian rollete, that will chose somebody to pay the bill")

names = (input("type the names, separeted by , . Ex Guilherme,Tata:"))

# coverting the string into list of strings
list_names = list(names.split(','))

lenght = len(list_names)

random_name = random.randint(0,lenght-1)

chosen = list_names[random_name]

print(f"Whos gonna pay the bill will be {chosen}")
