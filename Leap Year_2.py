year = int(input("Which year do you want to check? : "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("not Leap year.")
    else:
        print("leap Year.")
else:
    print("not Leap Year.")