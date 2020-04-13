'''
Author: Derek Martin
Credit: CIS 122 Lab
Description: Develop calendar related functions
'''

def get_full_month(num):
    '''
    Determines the month based on any input 1-12

    Prints the full name of the month

    Args:
        num (int): The number that corresponds with a month

    Returns:
        A blank print statement
    '''
    if (num == 1):
        print("January")
    elif (num == 2):
        print("February")
    elif (num == 3):
        print("March")
    elif (num == 4):
        print("April")
    elif (num == 5):
        print("May")
    elif (num == 6):
        print("June")
    elif (num == 7):
        print("July")
    elif (num == 8):
        print("August")
    elif (num == 9):
        print("September")
    elif (num == 10):
        print("October")
    elif (num == 11):
        print("November")
    elif (num == 12):
        print("December")
    else:
        print("Must be an integer between 1 and 12 (" + str(num) + " is invalid)")
        print(num)
        return print("", end="")

# Test        
# get_full_month(10)
# get_full_month(3)
# get_full_month(13)

def test_get_full_month():
    '''
    Tests get_full_month() using range of 14

    Uses chained conditionals with the range of 14 (0 - 13) to print the corresponding outputs.

    Args:
        None

    Returns:
        None
    '''
    for i in range(14):
        get_full_month(i)
    return

# Test
# test_get_full_month()

def is_leap_year(year):
    '''
    Accepts a year and determines whether it is a leap year or not

    Uses chained conditionals to do an in depth check on the input. This determines whether that year is a leap year.

    Args:
        year (int): The year to be checked

    Returns:
        True or False value (string): Whether the year is a leap year (true) or not (false)
    '''
    if ((year % 4) == 0) and ((year % 100) == 0) and ((year % 400) == 0):
         return True
    elif ((year % 4 == 0) and ((year % 100) != 0)):
         return True
    else:
        return False


def test_is_leap_year(start_year, end_year):
    '''
    Tests is_leap_year function by inputting start and end year integer arguments

    Runs a loop through every year in between the start and end year, and tests each year

    Args:
        start_year (int): the first year in the sequence of tests
        end_year (int): the last year in the sequence

    Returns:
        
    '''
    for i in range(start_year, end_year + 1):
        if (is_leap_year(i)):
            print(i)
        else:
            (print("", end=""))

    return

# Test
# test_is_leap_year(1996, 2112)
