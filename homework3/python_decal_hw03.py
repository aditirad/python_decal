
"""Python Decal HW03


1. Oski Stole Your Power

Oski hacked your computer and you can no longer use x**y or pow(x, y). Find
a different way (by writing a function) that can compute x raised to the power of y.

>>> x = 2

>>> y = 3

>>> computePower(x, y)

8
"""

def computePower(x, y):
    result = 1
    for _ in range(y):
        result *= x
    return result

"""2. What Should I Wear?

You are trying to decide what to wear to the Python DeCal lecture, but you are only concerned about the day’s lowest and highest temperatures. Write a function that takes in a list as input and returns a tuple with the min and max as two values.

>>> readings = [15, 14, 17, 20, 23, 28, 20]

>>> temperatureRange(readings)

(14, 28)
"""

def computePower(x, y):
    result = 1
    for i in range(y):  # Repeat y times
        result = result * x  # Multiply result by x
    return result

def temperatureRange(readings):
    smallest = min(readings)  # low num
    biggest = max(readings)  # high num
    return (smallest, biggest)

"""3. Check if its the Weekend

All your classes have assigned problem sets due next week, and you want to
check if its the weekend so you have time to work on them. Write a function
that takes a day of the week (represented as an integer, where 1 = Monday, 2
= Tuesday, etc) and returns True if its a weekend and False if otherwise.
>>> day = 6 # Saturday
>>> isWeekend(day)

True
"""

def isWeekend(day):
    if day == 6 or day == 7:  # Check if it's Saturday or Sunday
        return True
    else:
        return False

"""4. Fuel Efficiency Calculator

The Python DeCal wants to take a trip to the Lick Observatory ( San Jose,
CA) and they want to pick the best car. Write a function that takes the distance
traveled (in miles) and the amount of fuel consumed (in gallons) as input and
returns the fuel efficiency.
>>> distance = 70 # miles

>>> fuel = 21.5 # gallons

>>> fuel_efficiency(distance, fuel)

3.26
"""

def fuel_efficiency(distance, fuel):
    efficiency = distance / fuel
    return round(efficiency, 2)

"""5. Secret Code

Write a function that takes an integer as input and moves its last digit to the
front of the number. You may NOT convert the input to a string. Hint: Try
modulus (%) and floor division. (\\) to solve this problem.
>>> n = 12345
>>> decodeNumbers(n)
51234
"""

def decodeNumbers(n):
    last_digit = n % 10
    remaining_number = n // 10 # Remove the last digit from the number
    new_number = last_digit * (10 ** (len(str(n)) - 1)) + remaining_number # Move the last digit to the front and multiply remaining number by 10 and add the last digit
    return new_number

"""6 Min & Max but with Loops!

Oh no! Oski hacked you computer again... now you have lost the ability to use
min() and max()

6.1 For Loops

Write two functions to manually find the minimum and maximum values in a list of numbers with for loops.

>>> nums = [2024, 98, 131, 2, 3, 72]

>>> find_min_with_for_loop(nums)

2

>>> find_max_with_for_loops(nums)

2024
"""

def find_min_with_for_loop(nums):
    min_num = nums[0] # first element as min

    for num in nums:
        if num < min_num:
            min_num = num  # Update if we find a smaller number

    return min_num

def find_max_with_for_loop(nums):
    max_num = nums[0] # first element as min

    for num in nums:
        if num > max_num:
            max_num = num  # Update if we find a larger number

    return max_num

"""6.2 While Loops
Write two functions to manually find the minimum and maximum values in a list of numbers with while loops.

>>> nums = [2024, 98, 131, 2, 3, 72]

>>> find_min_with_while_loop(nums)

2

2

>>> find_max_with_while_loops(nums)

2024
"""

def find_min_with_while_loop(nums):
    min_num = nums[0] # first element as min
    index = 1  # Start from second element

    while index < len(nums):
        if nums[index] < min_num:
            min_num = nums[index]  # Update if we find a smaller number
        index += 1  # Move to the next element

    return min_num

def find_max_with_while_loop(nums):

    max_num = nums[0] # first element as min
    index = 1  # Start from second element

    while index < len(nums):
        if nums[index] > max_num:
            max_num = nums[index]  # Update if we find a larger number
        index += 1  # Move to the next element

    return max_num

"""7 Counting Vowels

Write a function that takes a string as an input and returns the number of vowels
in the string and the number of consonants in the string as tuple. Dont forget
about capital letters! Hint: You can use .isalpha() to check if a character is a letter.

>>> text = "UC Berkeley, founded in 1868!"

>>> vowel_and_consonant_count(text)

(4, 11)
"""

def vowel_and_consonant_count(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for char in text:
        if char.isalpha():  # Checking if character is a letter
            if char in vowels:
                vowel_count += 1  # If it's a vowel, increment the vowel count
            else:
                consonant_count += 1  # If it's a consonant, increment the consonant count

    return (vowel_count, consonant_count)

"""8 Calculate Digital Root

Write a function that takes an integer as an input and returns the sum of its
digits.

>>> num = 2468

>>> digital_root(num)

20
"""

def digital_root(num):
    total = 0

    while num > 0:
        total += num % 10  # Add the last digit to the total
        num //= 10  # Remove the last digit

    return total
