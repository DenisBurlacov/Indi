salary = int(input())
if salary >= 20000:
    persent = salary / 100 * 13
    salary_minus_persent = salary - persent
    print(salary_minus_persent)
else:
    print(salary)