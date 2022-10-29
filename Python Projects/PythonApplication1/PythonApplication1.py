from typing import Text


leapYear = False

year = int(input("Year: "))
day = int(input("Day: "))
simplifiedDay = 0

monthName = ()


if(year % 4 == 0):
    leapYear = True
    if(year % 100 == 0):
        leapYear = False
        if(year % 400 == 0):
            leapYear = True
else:
    leapYear = False

if leapYear == True:
    if day in range(1, 31):
        monthName = "January"
        simplifiedDay = day
    elif day in range(32, 59):
        monthName = "Febuary"
        simplifiedDay = day - 31
    elif day in range(60, 90):
        monthName = "March"
        simplifiedDay = day - 59
    elif day in range(91, 120):
        monthName = "April"
        simplifiedDay = day - 90
    elif day in range(121, 151):
        monthName = "May"
        simplifiedDay = day - 120
    elif day in range(152, 181):
        monthName = "June"
        simplifiedDay = day - 151
    elif day in range(182, 212):
        monthName = "July"
        simplifiedDay = day - 181
    elif day in range (213, 243):
        monthName = "August"
        simplifiedDay = day - 212
    elif day in range (244, 273):
        monthName = "September"
        simplifiedDay = day - 243
    elif day in range(274, 304):
        monthName = "October"
        simplifiedDay = day - 273
    elif day in range(305, 334):
        monthName = "November"
        simplifiedDay = day - 304
    elif day in range(335, 367):
        monthName = "December"
        simplifiedDay = day - 335
    else:
        print(year, " Only has 366 days in a year")
else:
    if day in range(1, 31):
        monthName = "January"
        simplifiedDay = day
    elif day in range(32, 58):
        monthName = "Febuary"
        simplifiedDay = day - 31
    elif day in range(59, 89):
        monthName = "March"
        simplifiedDay = day - 58
    elif day in range(90, 119):
        monthName = "April"
        simplifiedDay = day - 89
    elif day in range(120, 150):
        monthName = "May"
        simplifiedDay = day - 119
    elif day in range(151, 180):
        monthName = "June"
        simplifiedDay = day - 150
    elif day in range(181, 211):
        monthName = "July"
        simplifiedDay = day - 180
    elif day in range (212, 242):
        monthName = "August"
        simplifiedDay = day - 211
    elif day in range (243, 272):
        monthName = "September"
        simplifiedDay = day - 242
    elif day in range(273, 303):
        monthName = "October"
        simplifiedDay = day - 272
    elif day in range(304, 333):
        monthName = "November"
        simplifiedDay = day - 303
    elif day in range(334, 366):
        monthName = "December"
        simplifiedDay = day - 332
    else:
        print(year, " Only has 365 days in a year")


if year < 0:
    print("Negative years aren't allowed")

if day <= 0:
    print("Days less than or equal to 0 aren't allowed")


print("That is", monthName, simplifiedDay,"th")
