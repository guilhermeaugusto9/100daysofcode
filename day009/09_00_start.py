programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}


print(programming_dictionary["Bug"])


# Create an empty dictionary

empty_dictionary = {}


# wipe an exsiting dictionary

programming_dictionary = {}

print(programming_dictionary)


# edit an item in a dictionary

programming_dictionary["Bug"] = "new definition of bug to show how edit"

print(programming_dictionary["Bug"])



# loop through a dictionary

for key in programming_dictionary:
	print(key)
	print(programming_dictionary[key])

	
	


