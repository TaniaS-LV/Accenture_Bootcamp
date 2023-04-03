# ------TASK 1 -------
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"Car's make: {self.make}, Car's model: {self.model}, Car's year: {self.year}"


car = Car('Ford', 'Focus', 2010)


# print(car.get_info())


# ------TASK 2 -------
class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


rectangle = Rectangle(5, 10)


# print(rectangle.area())
# print(rectangle.perimeter())


# ------TASK 3 -------
class BankAccount():
    def __init__(self, account_number, balance, owner_name):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


bank_account = BankAccount(123, 345.50, 'Tatjana')
bank_account.withdraw(45.50)


# print(f"{bank_account.balance:.2f}")


# ------TASK 4 -------
class Person():
    def __init__(self, name: str, age: int, address: str):
        self.name = name
        self.age = age
        self.address = address

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}"


person = Person('John', 35, "London")


# print(person.get_info())


# ------TASK 5 -------
class Animal():
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return "Unknown sound"


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


cat = Cat('Alice', 'Felis Catus')


# print(cat.speak())

# Alternative solution
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        sounds = {
            'dog': 'Woof',
            'cat': 'Meow',
            'cow': 'Moo',
            'bird': 'Tweet'
        }
        return sounds.get(self.species, 'Unknown sound')


animal = Animal('Rex', 'dog')


# print(animal.speak())


# ------TASK 6 -------
class Vehicle():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def get_info(self):
        return f"{super().get_info()} - {self.num_doors} doors"


class Truck(Vehicle):
    def __init__(self, make, model, year, payload_capacity):
        super().__init__(make, model, year)
        self.payload_capacity = payload_capacity

    def get_info(self):
        return f"{super().get_info()} - {self.payload_capacity} t payload capacity"


truck = Truck('Volvo', 'FH16', 2013, 500)
# print(truck.get_info())
car = Car('Toyota', 'Yaris', 2015, 4)


# print(car.get_info())


# ------TASK 7 -------
class Person():
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def get_info(self):
        return f"{self.name}, aged {self.age}, lives in {self.address}"


class Student(Person):
    def __init__(self, name, age, address, level):
        super().__init__(name, age, address)
        self.level = level

    def get_info(self):
        return f"{super().get_info()}, studies at level {self.level}"


class Teacher(Person):
    def __init__(self, *args, subject, **kwargs):
        super().__init__(*args, **kwargs)
        self.subject = subject

    def get_info(self):
        return f"{super().get_info()}, teaches {self.subject}"


student = Student('John', 10, 'London', 4)
# print(student.get_info())
teacher = Teacher('Abigail', 45, 'London', subject='Chemistry')
# print(teacher.get_info())


# ------TASK 8 -------
# Write a Python program that reads a JSON file containing a list of dictionaries, sorts the list by a specific key, and writes the sorted list back to the file.
import json

with open("input_files/data.json", "r") as f:
    data = json.load(f) #convert json
    # print(data) #print list of dictionaries

data_sorted = sorted(data, key=lambda d: d['name'])
# print(data_sorted) #print sorted list

with open('input_files/data.json', 'w') as file:
    json.dump(data_sorted, file)  # convert to json and write the sorted list back to the file


# ------TASK 9 -------
#Write a Python program that reads a CSV file containing student grades, calculates their average score, and writes the average to a new file
with open("input_files/grades.csv", "r") as f:
    header = f.readline() #discards the headline and starts the loop with the next line
    results = []
    for line in f:
        fields = line.strip().split(',')
        name = fields[0]
        grades = [int(i) for i in fields[1:len(fields)]]
        average = sum(grades) / len(grades)
        result = f'{name},{average}\n'
        results.append(result)

with open("input_files/results.csv", "w") as f:
    f.write('Name,Average\n')
    f.writelines(results)


# ------TASK 10 -------
#Write a Python program that reads a CSV file containing student grades and writes a new CSV file with the grades sorted by student name.

with open("input_files/grades.csv", "r") as f:
    header = f.readline()
    results = []
    for line in f:
        fields = line.strip().split(',')
        name = fields[0]
        grades = [int(i) for i in fields[1:len(fields)]]
        result = [name]
        result.extend(grades)
        results.append(result)

sorted_results = sorted(results, key = lambda x:x[0])

with open("input_files/sorted_grades.csv", "w") as f:
    f.write(header)
    for row in sorted_results:
        csv_row = ",".join(str(value) for value in row)
        f.write(csv_row + "\n")


