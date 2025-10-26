'''# Asking user for their name and removes whitespace from str and capitalize

name = input("What's your name? ").strip().title()

# using split to seperate values
first, last = name.split(" ")

# Say hello to user using f formatting string
print(f"hello, {first}")

# Printing name
print(name) '''

'''
# using int in the code as a function that has the input function in it
x = int(input("What's x?"))
y = int(input("What's y?"))

print(x + y)
'''
# using float in the code as i used int earlier
x = float(input("What's x?"))
y = float(input("What's y?"))

print(x + y)