def is_armstrong(num):

    num_str = str(num)

    num_digits = len(num_str)
    

    armstrong_sum = 0
    
 
    for digit in num_str:
        # Convert the digit back to an integer
        digit_int = int(digit)
        # Add the nth power of the digit to the sum
        armstrong_sum += digit_int ** num_digits
    
    # Check if the sum is equal to the original number
    return armstrong_sum == num

# Test the function
input_num = int(input("Enter a number: "))
if is_armstrong(input_num):
    print("Yes, it's an Armstrong number.")
else:
    print("No, it's not an Armstrong number.")