# Problem Set 7
# Program: Working 9 to 5
# Alexis Varas Ortiz
# Description: Convert time from 12-hour format to 24-hour format
import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    # Catch any errors relating to the regex
    except re.error as e:
        print("Invalid regular expression...", e)
        sys.exit(1)


def convert(s):
    # Check for pattern. True if it matches
    if match := re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$", s, re.IGNORECASE):
        #Assign the group values to the respective variables
        start_hour, start_minute, start_period = match.group(1, 2, 3)
        end_hour, end_minute, end_period = match.group(4, 5, 6)

        # If no minutes where found in string, assign 0 to these variables
        if not start_minute:
            start_minute = 0
        if not end_minute:
            end_minute = 0

        # Validating minutes and converting hour format.
        # Converted arguments to int to eventually return an int value from the function
        start_minute, end_minute = validate_time(int(start_minute), int(end_minute))
        start_hour, end_hour = convert_hours(int(start_hour), int(end_hour), start_period, end_period)

        return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"


    # If pattern does not match, raise ValueError
    else:
        raise ValueError("Incorrect Format")


# Verify the minutes inputted are valid, no greater than 59
def validate_time(minute1, minute2):
    if minute1 > 59 or minute2 > 59:
        raise ValueError("Invalid time")

    return minute1, minute2


# Convert hours to 24-hour equivalent
def convert_hours(hour1, hour2, period1, period2):
    # Verify valid hour is input, no greater than 12
    if hour1 > 12 or hour2 > 12:
        raise ValueError("Invalid time")

    # Convert 12 AM properly to 24-hour format
    if period1 == "AM" and hour1 == 12:
        hour1 = 0
    if period2 == "AM" and hour2 == 12:
        hour2 = 0

    # Convert hours to 24-hour format if in the afternoon
    # Exclude when 12 PM
    if period1 == "PM" and hour1 != 12:
        hour1 += 12
    if period2 == "PM" and hour2 != 12:
        hour2 += 12

    return hour1, hour2



if __name__ == "__main__":
    main()
