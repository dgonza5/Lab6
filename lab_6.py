



"""
To start, we will generate a random integer between 1 and 20, and 
based on the result of the random numner,  we check to see if it falls under certain range
if the numnber is greater than 15, than the result will be "Cherries"
otherwise if the number is > 10, then the result will be "Orange"
otherwise if the number is > 5, then the result will be "Plum"
otherwise if the number is > 2, then the result will be "Melon"
otherwise if the number is > 1, then the result will be "Bell"
if the number is not any of the above, then the result will be "Bar"

we iterate over using a loop three times and print the results to the user. As an example "Plum Cherries"

"""

"""
num = gereate random number

if num is greater than 15, 
    then the result will be "Cherries"
otherwise if num is > 10, 
    then the result will be "Oranges"
otherwise if num is > 5, 
    then the result will be "Plum"
otherwise if num is > 2, 
    then the result will be "Melon"
otherwise if num is > 1, 
    then the result will be "Bell"
otherwise
    the result will be "Bar"

loop three times
    print the output (fruit) to the user 

"""

import random

def main():
    for i in range(0, 3):
        # print('i--->', i)
        spin()

def spin():
    rand_um = random.randint(1, 20)
    output = ""
    if(rand_um > 15):
        output = "Cherries"
    elif(rand_um > 10):
        output = "Orange"
    elif(rand_um > 5):
        output = "Plum"
    elif(rand_um > 2):
        output = "Melon"
    elif(rand_um > 1):
        output = "Bell"
    else:
        output = "Bar"
    
    print(output, end=" ")

main()