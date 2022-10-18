"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        if len(numbers)%2==0:
            first_middle=int(len(numbers)/2)-1
            second_middle=int(len(numbers)/2)
            median= (numbers[first_middle]+ numbers[second_middle])/2

        else:
            position_median= int(len(numbers)/2)
            median= numbers[position_median]

    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

print(f'The median of {numbers} is {median}')
