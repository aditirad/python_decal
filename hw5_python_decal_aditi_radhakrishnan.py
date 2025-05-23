"""HW5_Python_Decal_Aditi_Radhakrishnan

# HW5 - Review

# 1. What command will tell you what your working directory is?
# pwd

# 2. What command will list all the files in your current working directory?
# ls

# 3. What commands will let you move to the correct repository and pull the latest changes?
# cd ~/python_decal/judy_decal
# git pull origin main

# 4. How would you move this new homework.py to your personal repository homework directory?
# mv homework.py ~/personal_repo/homework/

# 5. What command(s) will let you see the contents of homework.py in your terminal?
# cat homework.py


# 6. What command will let you edit the contents of homework.py in your terminal?
# vim homework.py

# 7. What commands will allow you to save the changes and push from local to remote repository?
# git add homework.py
# git commit -m "Completed HW5"
# git push origin main

# 8. How to resolve the git error and explanation?
# git pull origin main --rebase
# git push origin main
# Explanation: Judys local repo is outdated compared to the remote. A pull is needed in order to sync the changes.

# 9. What absolute path will allow you to move to Recents/?
# cd ~/Recents/
"""

# 2.1 Data Types

def checkDataType(value):
    """Returns the data type of the input as a string."""
    return type(value).__name__

#2.2 Conditionals
def evenOrOdd(num):
    """Returns 'Even' if num is even, 'Odd' otherwise."""
    return "Even" if num % 2 == 0 else "Odd"

#3 Loops
def sumWithLoop(lst):
    """Returns the sum of a list using a loop."""
    total = 0
    for num in lst:
        total += num
    return total

# 4.1 Lists
def duplicateList(lst):
    """Returns a new list with each element duplicated."""
    new_list = []
    for item in lst:
        new_list.extend([item, item])
    return new_list


# 4.2 Debugging
def square(num):
    """Returns the square of a number."""
    return num * num
