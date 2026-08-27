def addRangeNumber(n):
    previous_number = 0

    for i in range(n):
        current_sum = i + previous_number
        yield f"Current Number {i} Previous Number {previous_number} Sum: {current_sum}"
        previous_number = i


# Calling the generator and iterating through the yielded results
for line in addRangeNumber(10):
    print(line)