# ------TASK 1 -------
# option 1
a = int(input("Enter an integer: "))
if a == 0:
    print('This number is zero')
elif a < 0:
    print('This number is negative.')
else:
    print('This number is positive. ')

# option 2
print('This number is zero' if (a := int(
    input("Enter an integer: "))) == 0 else 'This number is negative.' if a < 0 else 'This number is positive.')

# ------TASK 2 -------
for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)

# ------TASK 3-------
b = int(input('Enter an integer: '))
for r in range(1, b + 1):
    if b % r == 0:
        print(r)

# ------TASK 4-------
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
op = ''
while op not in ['*', '/', '+', '-', '%']:
    op = input('What type of operation do you want to perform: Type *,/,+,- or %: ')
    if op not in ["*", "/", "+", "-", "%"]:
        print("Operation provided isn't valid, please,try again.")

# ------TASK 5-------
num = int(input('Enter a number: '))
for n in range(2, num):
    if num % n == 0:
        print('This is not a prime number')
        break
else:
    print('This is a prime number.')
