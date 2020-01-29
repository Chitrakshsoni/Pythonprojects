a = int(input("Enter a year: "))
if a%4==0 :
    if a%100==0:
        if a%400==0:
            print("It is a leap year ")
        else:
            print("Not a leap year")
    else:
        print("It is a leap year")
