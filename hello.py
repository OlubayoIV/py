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
    print('x is not equal than y')

score = int(input('Score: '))

if score >= 90:
    print("Grade: A")
elif score >= 80 and score < 90:
    print('Grade: B')
elif score >= 70:
    print('Grade: C')
elif score >= 60 and score <70:
    print('Grade: D')
else:
    print('Grade: F')

#realizing even or odd numbers using if and else
x = int(input('What is x? '))
if x % 2 == 0:
    print("Even")
else:
    print('Odd')


#using match to nmake codes shorter (this is case sensitive)
name = input("What's your name? ")

match name:
    case 'Ayo' | 'Yo' | 'Indeed':
        print('Emea')
    case 'Ayo':
        print('Afea')
#creating a loop using while
i = 0
while i < 3:
    print("meow")
    i += 1
#containing multiple values using list and for loops
for i in [0, 1, 2]:
    print('meow')

#containing multiple values using range and for loops
#range expects integer so it doesn't work with str except there is another command to help it work
while True:
    n = int(input('Whats n? ')) 
    if n > 0:
        break

for _ in range(n):
    print('meow')

students = ['jazz', 'amy', 'leo']

for student in students:
    print(student)'''

#using dict
students = {
    'Hermione': 'Gryffindor',
    'Heone': 'Gryfor',
    'Hermne': 'Grindor'
    }

print(students['Hermione'])