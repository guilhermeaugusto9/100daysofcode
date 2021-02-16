import random
#import my_module1    #the module I created in another file

#print(my_module1.pi) test of import the custom module

random_integer = random.randint(1,10)
print(random_integer)

random_float = random.random()  # if you dont put nothing intro, always will generate a number between 0 and 1
print(random_float)


love_score = random.randint(1,100)
print(f"Your love score is {love_score}")



