person = {}
s = "IVANOV IVAN 19 Samara SGU 4 5 5 5 4 3 5 3"
s = s.split()
print(s)
print("--//" * 20)
person['Last_name'] = s[0]
person['first_name'] = s[1]
person['age'] = s[2]
person['city'] = s[3]
person['university'] = s[4]
print(person)
print("--//" * 20)
person['marks'] = []
for i in s[5:]:
    person['marks'].append(int(i))
print(person)
