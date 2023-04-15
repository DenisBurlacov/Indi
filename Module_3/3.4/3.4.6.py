user_pass = input()
pass_confirm = input()
if len(user_pass) < 7:
    print("Short")
elif user_pass != pass_confirm:
    print('Difference')
else:
    print('OK')