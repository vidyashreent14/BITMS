def is_palindrome(s):

    s = s.lower()

    s = s.replace(" ", "")

    reversed_s = s[::-1]

    return s == reversed_s


input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")