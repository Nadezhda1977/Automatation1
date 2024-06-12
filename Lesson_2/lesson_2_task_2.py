year = int(input('Введите год: '))
def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False

is_leap = is_year_leap(year)
print("год", year, ":", is_leap)

