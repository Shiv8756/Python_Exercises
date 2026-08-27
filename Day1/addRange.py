def addRangeNumber(n):
    previous_number=0
    for i in range(n):
        sum=i+previous_number
        print(f"Current Number {i} Previous Number {previous_number} Sum: {sum}")
        previous_number=i



addRangeNumber(10)