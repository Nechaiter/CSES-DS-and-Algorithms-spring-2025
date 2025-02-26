def check_year(year):
    to_string=str(year)
    first_two=int(to_string[:2])
    last_two=int(to_string[2:])
    if (first_two+last_two)**2==year:
        return True
    return False


print(check_year(1995)) # False
print(check_year(2024)) # False
print(check_year(2025)) # True
print(check_year(2026)) # False
print(check_year(3025)) # True
print(check_year(5555)) # False