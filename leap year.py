def is_leap_year(year):
    # Leap year is divisible by 4
    # If the year is divisible by 100, it must also be divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Test the function
input_year = int(input("Enter a year: "))
if is_leap_year(input_year):
    print("Yes, it's a leap year.")
else:
    print("No, it's not a leap year.")