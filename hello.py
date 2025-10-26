'''# Asking user for their name and removes whitespace from str and capitalize

name = input("What's your name? ").strip().title()

# using split to seperate values
first, last = name.split(" ")

# Say hello to user using f formatting string
print(f"hello, {first}")

# Printing name
print(name) '''

x = input("What's x?")
y = input("What's y?")

z = x + y

print(z)