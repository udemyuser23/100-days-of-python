year = int(input("Which year do you want to check? : "))

if year % 4 == 0:
    print("{0} is a leap year. ".format(year))
elif year % 100 == 0:
    print("{0} is a leap year. ".format(year))
else:
    print("{0} is not a leap year. ".format(year))