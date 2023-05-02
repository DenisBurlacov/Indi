# from pprint import pprint
# a = [["test", 12], ["test_1", 23], ["test)", 234]]
# c = dict(a)
# pprint(c)
person = {}
s = "Ivanow Ivan Kharkiv KPY 5 5 5 5 5 5"
s = s.split()
person['Last_Name'] = s[0]
person['First_Name'] = s[1]
person["Sity"] = s[2]
person["University"] = s[3]
person["marks"] = []
for i in s[4:]:
    person["marks"].append(int(i))

print(s)
print(person)
print(len(person))
for i in person:
    print(i, person[i])