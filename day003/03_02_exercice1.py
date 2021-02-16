number = int(input("Which number do you want to check?  "))
# the symbol % will divide and show the remaining number


test = number % 2

if test >= 1:
    print(f"you type an odd number {number} with rest {test}")
else:
    print(f"you typed an even number {number} with no rest ")


