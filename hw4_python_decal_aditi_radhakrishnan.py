
"""HW4_Python_Decal_Aditi_Radhakrishnan

2.1 Making a List Variable

Create a variable (name it anything you want, but make it descriptive!) that
is assigned to a list with numbers 0 through 20. You should not write each
number manually.

>>> whateverNameYouWant = # Your code here

>>> print(whateverNameYouWant)

[0, 1, 2, ..., 20] # It should print all numbers 1-20 in a list
"""

# 2.1 Making a List Variable
numbers_list = list(range(21))
print(numbers_list)  # [0, 1, 2, ..., 20]

"""2.2 Working with List Elements

Write a function that will take in your list from Part 2.1 and square each element in the list. Assign the result to a new variable.

>>> whateverNameYouWant = # Your code from Part 2.1

>>> def squareList():

>>> # Your code here

>>> anotherNameYouWant = squareList(list)

>>> print(anotherNameYouWant)

[0, 1, 4, ..., 400]
"""

# 2.2 Squaring List Elements
def square_list(lst):
    """Takes a list and returns a new list with each element squared."""
    return [x ** 2 for x in lst]

squared_list = square_list(numbers_list)
print(squared_list)  # [0, 1, 4, ..., 400]

"""2.3 Slicing

Write a function that takes in your new list from Part 2.2 and returns the first
15 elements of the list using slicing.
>>> anotherNameYouWant = squareList(list)
>>> first_fifteen_elements(anotherNameYouWant)
[0, 1, 4, ..., 196]
"""

# 2.3 Slicing First 15 Elements
def first_fifteen_elements(lst):
    """Returns the first 15 elements of a list."""
    return lst[:15]

print(first_fifteen_elements(squared_list))  # [0, 1, 4, ..., 196]

"""2.4 Striding

Write a function that takes in your list from Part 2.2 and returns every 5th
element from the list using striding.
>>> anotherNameYouWant = squareList(list)
>>> every_fifth_element(anotherNameYouWant)
[16, 81, 196, 361]
"""

# 2.4 Striding Every 5th Element
def every_fifth_element(lst):
    """Returns every 5th element from a list."""
    return lst[4::5]  # Starts at index 4 (5th element), strides by 5

print(every_fifth_element(squared_list))  # [16, 81, 196, 361]

"""2.5 Slicing & Striding

Write a function that takes your list from Part 2.2, slices the last 3 elements of
the list, and then returns every 3rd element from that list in reverse order.
>>> anotherNameYouWant = squareList(list)
>>> fancy_function(anotherNameYouWant)
[400, 289, 196, 121, 64, 25, 4]
"""

# 2.5 Slicing & Striding in Reverse
def fancy_function(lst):
    """Slices the last 3 elements, then returns every 3rd element in reverse order."""
    return lst[-21:: -3]  # Takes last 21 elements and strides backwards by 3

print(fancy_function(squared_list))  # [400, 289, 196, ..., 4]

"""3.1 Creating a 5x5 2D List

Write a function that uses nested for loops to create a 5x5 2D list where the
numbers 1 through 25 are stored sequentially. Assign the result to a new variable.
>>> matrix = create_2d_list()
>>> print(matrix)
[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
[16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
"""

# 3.1 Creating a 5x5 2D List
def create_2d_list():
    """Creates a 5x5 2D list with numbers 1 through 25 sequentially."""
    return [[i + j * 5 + 1 for i in range(5)] for j in range(5)]

matrix = create_2d_list()
print(matrix)

"""3.2 Replacing 2D List with Multiples of 3

With the 2D list you created in Part 3.1, write a function that will replace all
multiples of 3 with the character “?”.
>>> matrix = create_2d_list()
>>> modified_2d_list(matrix)
[[1, 2, ‘?’, 4, 5],
[‘?’, 7, 8, ‘?’, 10],
[11, ‘?’, 13, 14, ‘?’],
[16, 17, ‘?’, 19, 20],
[‘?’, 22, 23, ‘?’, 25]]
"""

# 3.2 Replacing Multiples of 3 with '?'
def modified_2d_list(matrix):
    """Replaces multiples of 3 in a 2D list with '?'."""
    return [['?' if num % 3 == 0 else num for num in row] for row in matrix]

new_matrix = modified_2d_list(matrix)
print(new_matrix)

"""3.3 Summing None-’ ?’ Elements

Assign the result of your function from Part 3.2 to a variable. Write a function
that will iterate through the new 2D list variable and return the sum of all the
elements that are not “?”. Hint: Try using “!=”.
>>> matrix = create_2d_list()
>>> new_matrix = modified_2d_list(matrix)
>>> sum_non_question_elements(new_matrix)
217
"""

# 3.3 Summing Non-'?' Elements
def sum_non_question_elements(matrix):
    """Sums all numeric elements in a 2D list, ignoring '?'."""
    return sum(num if num != '?' else 0 for row in matrix for num in row)

print(sum_non_question_elements(new_matrix))  # Expected: 217
