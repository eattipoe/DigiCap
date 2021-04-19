"""
File: khansole_academy.py
-------------------------
Khansole Academy is a program that teaches users how to add by asking users to input answers for the addition of two
randomly generating integers between 10 and 99 inclusive. The program returns feedback based on the User's answers.

"""

import random
# use code below  to generate a random integer between 30 and 50 for example
#print(random.randint(30, 50))

# ********************************** YOUR CODE GOES BELOW HERE *********************************************************

print("Mastering two(2) digits addition:")
count = 0

while True:
    #assigning values to capture random numbers
    number_1 = random.randint(10, 99)
    number_2 = random.randint(10, 99)
    
    print("What is {} + {}?".format(number_1, number_2))
    answer = number_1 + number_2

    #capture user answer 
    user_answer = int(input('Your Answer: '))
    if user_answer == answer:

        #if the user answer is right, increase counter by 1
        count += 1
        print("Correct! You've gotten {} correct in a row".format(count))

        # until a user get the answer right in 3 successive rows, they keep attempting 
        if count < 3:
            continue

        # message dislayed to the user if the user gets it right 3 times in a row
        else:
            print("Congratulations! You mastered addition")
            break
    else:
        count = 0
        print('Incorrect. The expected answer is {}'.format(answer))

