# Problem Set 8
# Program: Seasons of Love
# Alexis Varas Ortiz
# Description: Calculate your age into minutes
from datetime import date, timedelta
import re , sys, inflect
p = inflect.engine()

def main():
    #Try block to verify birthdate is in the correct format
    try:
        year, month, day = input("Date of Birth: ").split("-")#If date is in the correct format it will split the string by each "-" and assign to each variable accordingly
        dob = date(int(year), int(month), int(day)) #converts input into a date object
    except ValueError: #If input is not in the correct format this error will be caught
        print("Invalid date")
        sys.exit(1)

    #Calls function to calculate age and converts the numeric value to the written English equivalent
    minutes = p.number_to_words(calculate_minutes(dob, date.today()))
    #Prints output after removing intances of the word "and"
    print(remove_and(minutes.capitalize()), "minutes")


#Calculates age and converts it to minutes
def calculate_minutes(dob, today):
    minutes = today - dob
    return int(minutes.total_seconds()/60)

#Removes intances of the word "and"
def remove_and(s):
    pattern = re.compile(r"(\s\b)and(\s\b)")
    return pattern.sub(' ', s)



if __name__ == "__main__":
    main()
