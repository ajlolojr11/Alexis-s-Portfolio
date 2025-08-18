'''
Problem Set 3
Program: Outdated
Alexis Varas Ortiz
'''

months = [
            "January", "February", "March",
            "April", "May", "June",
            "July", "August", "September",
            "October", "November", "December"
            ]

def main():

    while True:
        date = input("Date: ")

        if written_month(date):
            print (convert_written(date))
            break

        elif mmddyyy(date):
            print (convert_mmddyyyy(date))
            break

def written_month(d):
    #Validate Month Day, Year format
    if "," not in d:
        return False

    #Catch value error if str is not split as expected or if day or year is not a valid int
    try:
        month_day, year = d.split(",")
        month, day = month_day.split()
        day = int(day)
        year = int(year)
    except ValueError:
        return False

    #Return False if month does not match an item in the list or if days is not within the proper range
    if month not in months:
        return False

    if not 1 <= day <= 31:
        return False

    else:
        return True

def mmddyyy(d):
    #Validate mm/dd/yyy format
    #Catch value error if str is not split as expected or if month, day, or year is not a valid int
    try:
        month, day, year = d.split("/")
        month = int(month)
        day = int(day)
        year = int(year)
    except ValueError:
        return False

    #Return False if month and days are not within the proper range
    if not 1 <= month <= 12:
        return False

    if not 1 <= day <= 31:
        return False

    else:
        return True

def convert_written(d):
    #Convert Month Day, Year format to YYYY-MM-DD
    #Catch value error if str is not split as expected or if day or year is not a valid int
    try:
        month_day, year = d.split(",")
        month, day = month_day.split()
        year = int(year)
        day = int(day)
    except ValueError:
        return "Invalid Date"
    else:
        return f"{year:04}-{months.index(month) + 1:02}-{day:02}"

def convert_mmddyyyy(d):
    #Convert MM/DD/YYYY format to YYYY-MM-DD
    #Catch value error if str is not split as expected or if month, day, or year is not a valid int
    try:
        month, day, year = d.split("/")
        month = int(month)
        day = int(day)
        year = int(year)
    except ValueError:
        return "Invalid Date"
    else:
        return f"{year:04}-{month:02}-{day:02}"


main()
