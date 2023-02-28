# Multiplication Calculator Using Vincent's Methodology

# Vincent's mental multiplication method for 2-digit by 2-digit numbers utilizes the following algorithm to succeed:
# 1. Multiply both of the integers in the ones place together, putting the ones digit at the very end.
# 2. Cross multiply the tens-digit of the first integer and the ones-digit of the second and vice-versa 
# and add the results. Add the tens place of the previous digit to the sum. Put the ones digit in front of
# the first digit derived from Step 1.
# 3. Multiply both of the leading digits and add that to the tens place of the previous digit. Put the number in front
# of the digits inputted in Step 2.

# This program utilizes a variety of cases to check if the method works.

import random

# Setting up the repeated test cases
cases = 0
match = 0
while cases < 10000:
    # Defining 10a+b and 10x+y
    a = random.randint(1,9)
    b = random.randint(0,9)
    x = random.randint(1,9)
    y = random.randint(0,9)
    
    # Storing each individual number alongside their multiplication result for reference
    numeral_one = 10*a + b
    numeral_two = 10*x + y
    expected_result = numeral_one * numeral_two
    
    # The actual multiplication involved
    by = (b * y) % 10
    middle = (a * y) + (b * x) + (((b * y) - by) / 10)
    
    # Explanation of the by section:
    # Since % gives the ones digit, if you subtract by%10 from by, you would only have
    # digits higher than ones. To remove the 0 at the end, you simply divide by 10.
    
    front = (a * x)
    product = 100*front + 10*middle + by
    
    # Match cases
    if product == expected_result:
        match += 1
    cases += 1

print("Percentage of cases matched: ", match/100, "%")
