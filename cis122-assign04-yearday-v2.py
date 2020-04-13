'''
Author: Derek Martin
Credit: CIS 122
Description: refactor v1 with functions through encapsulation and generalization
'''
def start():
    '''
    Runs the program

    Defines each function when called

    Args: None

    Returns: None  
    '''
    def is_leap_year(year):
        '''
        Accepts a year and determines whether it is a leap year or not

        Uses chained conditionals to do an in depth check on the input. This determines whether that year is a leap year.

        Args:
            year (int): The year to be checked

        Returns:
            True or False value (boolean): Whether the year is a leap year (true) or not (false)
        '''
        year = int(year)
        if ((year % 4) == 0) and ((year % 100) == 0) and ((year % 400) == 0):
             return True
        elif ((year % 4 == 0) and ((year % 100) != 0)):
             return True
        else:
            return False

    def valid_year(year):
        '''
        Determines whether a year is valid or not

        Accepts a year and tests whether the year makes sense

        Args: year (int): The year to be checked

        Returns:
            True or False value (boolean): Whether the year is valid (true) or not (false)
        '''
        if int((year) <= 0):
            print("Year must be > 0")
            return False
        else:
            return True

    def valid_day_of_year(year, day_of_year):
        '''
        Determines whether a day is valid or not

        Accepts a day and tests whether the day makes sense

        Args: day (int): The day to be checked

        Returns:
            True or False value (boolean): Whether the day is valid (true) or not (false)
        '''
        if (int(day_of_year) <= 0):
            print("Day of year must be > 0")
            
        def get_days_in_year(year):
            '''
            Determines the number of days in a given year

            First determines whether the year is a leap year, and calculates accordingly
            
            Args:
                year (int): The year to be used to determine the number of days
            
            Returns:
                days_in_year (int): The number of days in that year
                0 (int): A value if the day is invalid
            '''
            days_in_year = 365
            if (is_leap_year(int(year))):
                days_in_year = days_in_year + 1
            if (int(day_of_year) > days_in_year):
                if (days_in_year == 365):
                    print("Day must be <= 365")
                    return 0
                else:
                    print("Day must be <= 366")
                    return 0
            else:
                return days_in_year

        if ((int(day_of_year) > 0) and (int(day_of_year <= get_days_in_year(year)))):
            return True
        else:
            return False

    def input_year():
        '''
        Prompts the user for a year

        Accepts input from the user and assigns it to a year variable

        Args:
            None

        Returns:
            year (int): The year input from the user
            0 (int): A value for an invalid year   
        '''
        year = int(input("Enter year: "))
        if (valid_year(year)):
            return year
        else:
            return 0

    def input_day_of_year(year):
        '''
        Prompts the user for a day of the year

        Accepts input from the user and assigns it to a day of year variable

        Args:
            year (int): Which year the day is in

        Returns:
            day_of_year (int): The day of the year input from the user
            0 (int): A value for an invalid day of the year   
        '''
        day_of_year = 1
        if (valid_year(year)):
            day_of_year = int(input("Enter day of year: "))
        if (valid_day_of_year(year, day_of_year)):
            return day_of_year
        else:
            return 0

    def valid_month(month):
        '''
        Determines whether a month is valid or not

        Determines whether the month makes sense

        Args:
            month (int): Which month to validate

        Returns:
            True or False (boolean): Whether the month is valiud or not
        '''
        if (0 < month <= 12):
            return True
        elif (month <= 0):
            print("Month must be > 0")
            return False
        else:
            print("Month must be <= 12")
            return False

    def translate_month(month):
        '''
        Translates the month to a string
        
        Gives the full name of the month
        
        Args:
            month (int): Which month to translate

        Returns:
            "" (string): if month is invalid
        '''
        if (valid_month(month)):
            if (month == 1):
                print("January")
            elif (month == 2):
                print("February")
            elif (month == 3):
                print("March")
            elif (month == 4):
                print ("April")
            elif (month == 5):
                print ("May")
            elif (month == 6):
                print ("June")
            elif (month == 7):
                print ("July")
            elif (month == 8):
                print ("August")
            elif (month == 9):
                print ("September")
            elif (month == 10):
                print ("October")
            elif (month == 11):
                print ("November")
            elif (month == 12):
                print ("December")
        else:
            return ""

    def get_days_in_month(year, month):
        '''
        Determines the number of days in the month

        Runs through nested conditionals and figures out the amount of days for each month

        Args:
            year (int): Which year the month is in
            month (int): Which month to get the days

        Returns:
            0 (int): if invalid
        '''
        if (valid_year(year)):
            if (valid_month(month)):
                if (is_leap_year(year)):
                    if (month == 2):
                        print("29")
                else:
                    if (month == 1):
                        print("31")
                    elif (month == 2):
                        print("28")
                    elif (month == 3):
                        print("31")
                    elif (month == 4):
                        print ("30")
                    elif (month == 5):
                        print ("31")
                    elif (month == 6):
                        print ("30")
                    elif (month == 7):
                        print ("31")
                    elif (month == 8):
                        print ("31")
                    elif (month == 9):
                        print ("30")
                    elif (month == 10):
                        print ("31")
                    elif (month == 11):
                        print ("30")
                    elif (month == 12):
                        print ("31")
            else:
                return 0
        else:
            return 0

    def valid_day(year, month, day_of_year):
        '''
        Determines whether a day is valid or not

        Tests whether the day makes sense given the year, month, and day

        Args:
            year (int): The year to be checked
            month (int): The month to be checked
            day_of_year (int): The day to be checked

        Returns:
            True or False value (boolean): Whether the day is valid (true) or not (false)
        '''
        if (is_leap_year(year)):
            if ((int(day_of_year) > 366) or (int(day_of_year) <= 0)):
                return False
        elif ((int(day_of_year) > 365) or (int(day_of_year) <= 0)):
            return False
        else:
            if ((valid_year(year) and valid_month(month))):
                return True
            else:
                return False

    def get_date_string(year, month, day_of_year):
        '''
        Prints the final output of the full date
        
        Prints the month, the day of the month, and the year in one string
        
        Args:
            year (int): The year to be printed
            month (int): The month to be printed
            day_of_year (int): The day to be printed            

        Returns:
            "" (string): if the date is invalid
        '''
        if (valid_year(year) and valid_month(month) and valid_day(year, month, day_of_year)):
            # get_days_in_year(year)
            if (is_leap_year(year)):
                days_in_year = 366
            else:
                days_in_year = 365
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

                if (year > 0) and (day_of_year <= x) and (day_of_month >= 0):
                    print(month_name, str(day_of_month) + ",", year)
        else:
            return print('')

    year = input_year()
    valid_year(year)
    day_of_year = input_day_of_year(year)
    valid_day_of_year(year, day_of_year)
    if(valid_year(year) and (valid_day_of_year(year, day_of_year))):
        if (is_leap_year(year)):
            month = (int(12 / (366 / day_of_year))) + 1
        else:
            month = (int(12 / (365 / day_of_year))) + 1
    get_date_string(year, month, day_of_year)

start()
