#We have to start with 100, because 100 is the first 3-digit number.
number = 100

while number < 1000: #I want the loop to end when we have gone through all positive 3-digit numbers.
    if number % 17 == 0: #17 divisor checker.
        print(number)
    number += 1