def leapYear(n):
    if (n%4==0 and n%100!=0) or n%4==0:
        print("Leap Year")
    else:
        print("Not Leap Year")

leapYear(2001)