from string import ascii_lowercase
alphabet = {}
value = 0
for i in ascii_lowercase:
    value += 1
    alphabet[i] = value
print(alphabet)
