'''
Author: Derek Martin
Credit: CIS 122
Description: Create a basic program with no functions that determines the precise date given the day of the year
'''

# Determine if year is leap year or not, using is_leap_year() function
def is_leap_year(year_x):
    '''
    Accepts a year and determines whether it is a leap year or not

    Uses chained conditionals to do an in depth check on the input. This determines whether that year is a leap year.

    Args:
        year (int): The year to be checked

    Returns:
        True or False value (string): Whether the year is a leap year (true) or not (false)
    '''
    year_x = int(year_x)
    if ((year_x % 4) == 0) and ((year_x % 100) == 0) and ((year_x % 400) == 0):
         return True
    elif ((year_x % 4 == 0) and ((year_x % 100) != 0)):
         return True
    else:
        return False
    
# Prompt user for year using input()
year = int(input("Enter year: "))

# Validate that year > 0
# If not, return error message
if int((year) <= 0):
    print("Year must be > 0")

# Prompt user for day of the year
day_of_year = 1
if (int(year) > 0):
    day_of_year = int(input("Enter day of year: "))

# Validate that day > 0
# If not, return error message
if (int(day_of_year) <= 0):
    print("Day of year must be > 0")
    
# Validate that day of year <= days in year (accounting for possible leap year)
# If not, return error message determined by the number od days in that year
days_in_year = 365
if (is_leap_year(int(year))):
    days_in_year = days_in_year + 1

if (int(day_of_year) > days_in_year):
    if (days_in_year == 365):
        print("Day must be <= 365")
    else:
        print("Day must be <= 366")
        
# Loop through number of months in a year
# Determine the number of days in each month
# Create a variable x that holds a cumulative count of days starting from the first day
# Check if the day of the year <= the value of the variable x
# If not, continue to loop
# For each month looped through, add the number of days in that month to the variable x's value
# Check again until day of year <= the value of the variable x
# Then, you're in the right month
# Once in the right month, subtract a value y from variable x so that x == days in that month
# Subtract same value y from day of year to find day of month
# Print (Month Day, Year)
for month in range(12):
    day_of_month = 0
    x = 0
    month_name = ""
    if (month == 0):
        month_name = "January"
        days_in_month = 31
        x = 31
        if (day_of_year <= x):
            y = x - days_in_month
            day_of_month = day_of_year - y
    elif (month == 1):
        month_name = "February"
        if(days_in_year == 366):
            days_in_month = 29
            x = 60
            if (day_of_year <= x):
                y = x - days_in_month
                day_of_month = day_of_year - y
        else:
            days_in_month = 28
            x = 59
            if (day_of_year <= x):
                y = x - days_in_month
                day_of_month = day_of_year - y
    elif (month == 2):
        month_name = "March"
        days_in_month = 31
        if(days_in_year == 366):
            x = 91
            if (day_of_year <= x):
                y = x - days_in_month
                day_of_month = day_of_year - y
        else:
            x = 90
            if (day_of_year <= x):
                y = x - days_in_month
                day_of_month = day_of_year - y
    elif (month == 3):
        month_name = "April"
        days_in_month = 30
        if(days_in_year == 366):
            x = 121
            if (day_of_year <= x):
                y = x - days_in_month
                day_of_month = day_of_year - y
        else:
            x = 120
            if (day_of_year <= x):
                y = x - days_in_month
                day_of_month = day_of_year - y
    elif (month == 4):
        month_name = "May"
        days_in_month = 31
        if(days_in_year == 366):
            x = 152
            if (day_of_year <= x):
                y = x - days_in_month
                day_of_month = day_of_year - y
        else:
            x = 151
            if (day_of_year <= x):
                y = x - days_in_month
                day_of_month = day_of_year - y
    elif (month == 5):
        month_name = "June"
        days_in_month = 30
        if(days_in_year == 366):
            x = 182
            if (day_of_year <= x):
                y = x - days_in_month
                day_of_month = day_of_year - y
        else:
            x = 181
            if (day_of_year <= x):
                y = x - days_in_month
                day_of_month = day_of_year - y
    elif (month == 6):
        month_name = "July"
        days_in_month = 31
        if(days_in_year == 366):
            x = 213
            if (day_of_year <= x):
                y = x - days_in_month
                day_of_month = day_of_year - y
        else:
            x = 212
            if (day_of_year <= x):
                y = x - days_in_month
                day_of_month = day_of_year - y
    elif (month == 7):
        month_name = "August"
        days_in_month = 31
        if(days_in_year == 366):
            x = 244
            if (day_of_year <= x):
                y = x - days_in_month
                day_of_month = day_of_year - y
        else:
            x = 243
            if (day_of_year <= x):
                y = x - days_in_month
                day_of_month = day_of_year - y
    elif (month == 8):
        month_name = "September"
        days_in_month = 30
        if(days_in_year == 366):
            x = 274
            if (day_of_year <= x):
                y = x - days_in_month
                day_of_month = day_of_year - y
        else:
            x = 273
            if (day_of_year <= x):
                y = x - days_in_month
                day_of_month = day_of_year - y
    elif (month == 9):
        month_name = "October"
        days_in_month = 31
        if(days_in_year == 366):
            x = 305
            if (day_of_year <= x):
                y = x - days_in_month
                day_of_month = day_of_year - y
        else:
            x = 304
            if (day_of_year <= x):
                y = x - days_in_month
                day_of_month = day_of_year - y
    elif (month == 10):
        month_name = "November"
        days_in_month = 30
        if(days_in_year == 366):
            x = 335
            if (day_of_year <= x):
                y = x - days_in_month
                day_of_month = day_of_year - y
        else:
            x = 334
            if (day_of_year <= x):
                y = x - days_in_month
                day_of_month = day_of_year - y
    else:
        month_name = "December"
        days_in_month = 31
        if(days_in_year == 366):
            x = 366
            if (day_of_year <= x):
                y = x - days_in_month
                day_of_month = day_of_year - y
        else:
            x = 365
            if (day_of_year <= x):
                y = x - days_in_month
                day_of_month = day_of_year - y

    if (day_of_year <= x) and (day_of_month >= 0):
        print(month_name, str(day_of_month) + ",", year)
