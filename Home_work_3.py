# Reference: https://www.kite.com/python/answers/how-to-convert-between-month-name-and-month-number-in-python


import datetime



month_number = (input('Pick a number between 1-12: '))



datetime_object = datetime.datetime.strptime(month_number, "%m")
month_name = datetime_object.strftime("%b")
print(month_name)

if month_name < "1" and month_name <= "12":
    print(month_name)
