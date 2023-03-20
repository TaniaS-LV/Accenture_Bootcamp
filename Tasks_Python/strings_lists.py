# ------TASK 1 -------
text = input('Enter a text: ').lower()
letter = input('Enter a letter: ').lower()
answer = text.count(letter)
print(f'Letter "{letter}" has {answer} occurrences in the text.\n')

# ------TASK 1.1 -------
print('\nOccurences in the text:')
text_unique = []
text_unique_count = []
for t in text:
    if t.isalpha() and t not in text_unique:
        text_unique.append(t)
for t in text_unique:
    print(f'{t}: {text.count(t)} times.')
    text_unique_count.append(text.count(t))

# ------TASK 2 -------
# Sorting without using sort()
text_sorted = [None] * 26
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
for t in text_unique:
    i = alphabet.index(t)
    text_sorted[i] = t
text_sorted = [e for e in text_sorted if e is not None]

# Alternative solution 1
text_sorted = []
text_unique_copy = text_unique.copy()
while text_unique_copy:
    min_value = text_unique_copy[0]
    for t in text_unique_copy:
        if t < min_value:
            min_value = t
    text_sorted.append(min_value)
    text_unique_copy.remove(min_value)

# Alternative solution 2
text_sorted = []
text_unique_copy = text_unique.copy()
while text_unique_copy:
    min_value = min(text_unique_copy)
    text_sorted.append(min_value)
    text_unique_copy.remove(min_value)

# Print occurences in alhpabet order
print('\nOccurences in alhpabetical order:')
for x in text_sorted:
    i = text_unique.index(x)
    print(f'{x}: {text_unique_count[i]}')

# #Print occurences in numerical order
print('\nOccurences in descending order:')
pairs = zip(text_unique, text_unique_count)
sorted_pairs = sorted(pairs, key=lambda x: x[1], reverse=True)
for pair in sorted_pairs:
    print(f"{pair[0]}: {pair[1]}")
