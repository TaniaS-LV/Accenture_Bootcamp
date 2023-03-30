# ------TASK 1 -------
def return_sum(a, b):
    """Write a function that takes two parameters (a and b) and returns their sum."""
    return a + b

# print(return_sum(5,9))


# ------TASK 2 -------
vowels = ['a', 'e', 'i', 'o', 'u']
def count_vowels(string):
    """Write a function that takes a string as a parameter and returns the number of vowels (aeiou) in the string."""
    vowels_count = 0
    for el in string:
        if el in vowels:
            vowels_count += 1
    return vowels_count

# print(count_vowels('This is my test string'))


# ------TASK 3 -------
def palindrome(string):
    """Write a function that takes a string as a parameter and returns True if the string is a palindrome and False otherwise"""
    letters = string.strip(',.').replace(" ", '').lower()
    reverse = letters[::-1]
    return reverse == letters

# print(palindrome('This is just a random test string.'))
# print(palindrome('A nut for a jar of tuna.'))
# print(palindrome('racecar'))


# ------TASK 4 -------
def check_even(l: list) -> list:
    """Write a function that takes a list of integers as a parameter and returns a list of only the even integers in the original list"""
    return [el for el in l if el % 2 == 0]

#print(check_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# ------TASK 5 -------
def target_sum(l:list, x):
    """Write a function that takes a list of integers and a target sum as parameters and returns a list of two integers from the original list that add up to the target sum."""
    result = []
    for n in range(len(l)):
        for el in range(n+1, len(l)):
            if l[n] +l[el] == x:
                result.append([l[n],l[el]])
    return result

# print(target_sum([0,1,2,3,4,5,6,7,8,9,10],10))
# print(target_sum([10,4,6,3,2,0,1,3,4], 8))


# ------TASK 6 -------
def int_product(l:list):
    """Write a function that takes a list of integers as a parameter and returns the product of all the integers in the list."""
    result = 1
    for n in range(len(l)):
        result *= l[n]
    return result

# print(int_product([1,2,3]))
# print(int_product([10,4,6,3,2,1,3,4]))


# ------TASK 7 -------
def even_keys(d:dict):
    """Write a function that takes a dictionary as a parameter and returns a list of all the keys in the dictionary that have an even value."""
    return [el for el in list(d.keys()) if d[el] % 2 == 0]

# print(even_keys({'a':2, 'b':3}))
# print(even_keys({'a':2, 'b':3, 'c':8}))


# ------TASK 8 -------
def new_dict(l:list):
    """Write a function that takes a list of dictionaries as a parameter and returns a new dictionary that contains the sum of the values for each key in the original dictionaries."""
    new_dict = dict()
    for dct in l:
        for key, value in dct.items():
            if key not in new_dict:
                new_dict[key] = value
            else:
                new_dict[key] += value
    return new_dict

# print(new_dict([{'a':1, 'b': 2}, {'c':3, 'd':4}, {'e':5, 'f': 6}]))
# print(new_dict([{'a':1, 'b': 4, 'c': 6}, {'a':2, 'c':5}, {'a':3}]))
#print(new_dict([{1:19,2:7,3:6},{1:19,2:7,3:6},{1:7,2:5,3:3}]))


# ------TASK 9 -------
def swap_tuple(t:tuple):
    """Write a function that takes a tuple as a parameter and returns a new tuple that has the first and last elements swapped."""
    return (t[-1],) + t[1:-1] + (t[0], )

#print(swap_tuple((0,1,2,3,4)))


# ------TASK 10 -------
def new_set(s:set):
    """Write a function that takes a set as a parameter and returns a new set that contains only the elements that are not divisible by 3."""
    new_set = set()
    for el in s:
        if el % 3 != 0:
            new_set.add(el)
    return new_set

#print(new_set({1,2,3,4,5,6,8,9,12}))
