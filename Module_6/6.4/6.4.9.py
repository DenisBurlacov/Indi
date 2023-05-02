from string import ascii_lowercase

alphabet = {}
counter = 0
for i in ascii_lowercase:
    counter += 1
    alphabet[i] = counter
print(alphabet)
