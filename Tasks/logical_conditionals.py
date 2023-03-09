# ------TASK 1 -------
age = int(input('What is your age? Please enter a number: '))
licence = input("Do you have a driver's licence? Type 'y' or 'n': ").lower()
result = age > 17 and licence =='y'
print(f'You are able to drive: {result}')

# ------TASK 2 -------
password = input('Create a password: ')
letters = list(password)
has_uppercase = any((letter.isupper() for letter in letters))
has_lowercase = any((letter.islower() for letter in letters))
has_number = any((letter.isnumeric() for letter in letters))
result = len(password)>8 and has_uppercase and has_lowercase and has_number
print(f'Password accepted: {result}')

# ------TASK 3 -------
a = int(input('Enter any number: ')) % 2
b = int(input('Enter any number once again: ')) % 2
result_both = a==0 and b==0
result_one = a== 0 or b ==0
print(f'Both numbers are even: {result_both} \nAt least one number is even: {result_one}')

# ------TASK 4 -------
year = int(input('Enter a year: '))
result = year % 400 ==0 or year % 4 == 0 and year % 100 !=0
print(f'Leap year: {result}')

# ------TASK 5 -------
day = int(input('Enter a number for day: '))
month = int(input('Enter a number for month: '))
year = int(input('Enter a number for year: '))
month_check = 1 <= month <= 12
if month in [4,6,9,11]:
    day_check = day == 30
elif month == 2:
    if year % 400 ==0 or year % 4 == 0 and year % 100 !=0:
        day_check = day == 29
    else:
        day_check = day == 28
else:
    day_check = day== 31
result = month_check and day_check
print(f'Date valid: {result}')


