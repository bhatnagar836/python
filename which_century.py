def century(year):
    return int((year - (year % 100)) / 100) + 1 if (year % 100) else int((year-(year % 100))/100)


