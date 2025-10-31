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

'''
# using float in the code as i used int earlier
x = float(input("What's x?"))
y = float(input("What's y?"))

z = x / y
print(z)
'''
'''#defining a function creates a function
def hello():
    print('hello') 

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n
main()

#using if and elif statement in python
x = int(input("What's x? "))
y = int(input("What's y? "))

#using > < == != with if else statements
if x == y:
    print('x is equal to y')
else:
    print('x is not equal than y') '''

score = int(input('Score: '))

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print('Grade: B')
elif score >= 70 and score <80:
    print('Grade: C')
elif score >= 60 and score <70:
    print('Grade: D')
else:
    print('Grade: F')