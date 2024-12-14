'''
Problem Set 1
Program: Meal Time
Alexis Varas Ortiz
'''

def main():
    #Ask user for a time. Format 24-hour '##:##',
    #or 12-hour '##:## a.m.' or '##:## p.m.'
    meal_time = input("What time is it? ")
    #Call function to convert input into a floa
    #Reassign that new value to meal_time
    meal_time = convert(meal_time)

    if 7 <= meal_time <= 8:
        print("breakfast time")
    elif 12 <= meal_time <= 13:
        print("lunch time")
    elif 18 <= meal_time <= 19:
        print("dinner time")
    else:
        return

def convert(time):
    #Splits the hours and minutes and assigns it to their respective variables
    hour, minute = time.split(":")

    #Converts hour value to float
    #Converts time from 12 to 24 hour format if necessary
    if minute[-4:] == "p.m.":
        hour = float(hour) + 12
    else:
        hour = float(hour)

    #Assigns the first 2 characters and converts them to float
    minute = float(minute[:2])

    #Divide the minutes by 60 to convert them to the
    #percentage/decimal equivalent of what it represents in an hour
    time = hour + minute / 60

    return time

if __name__ == "__main__":
    main()

