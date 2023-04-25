s = input()
user_string = list(input().split())
n = len(user_string)
for i in range(n):
    if s in user_string[i].lower():
        print(user_string[i])