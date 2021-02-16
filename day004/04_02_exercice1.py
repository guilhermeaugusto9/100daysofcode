import random

print("Welcome to the head or tail game")

want = (input("do you want to play? (Y, N)"))

if want == 'Y':
	random_integer = random.randint(0, 1)
	if random_integer == 1:
		print(' You got a Head')
	else:
		print("You got a Tail")
else:
	print("have a nice day motherfocker")

