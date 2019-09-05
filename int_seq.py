#Variables that will store data from the user.
count = 0
summary = 0
even = 0
odd = 0
largest = 0
current = 1 #Note that 'current' must start with the value 1 otherwise the loop will never start.

#A loop that will end when the user types in either 0 or less than zero.
while current > 0:
    current = int(input('Enter an integer: '))

    #The listener for 0 or less
    if current <= 0:
        break

    #If count is 0, the end result will not display.
    count += 1

    #Even or odd numbers counter
    if current % 2 == 0:
        even += 1
    else:
        odd += 1
    
    #Listener for the largest number
    if current > largest:
        largest = current

    #Sum of all numbers
    summary += current
    print('Cumulative total: ', summary)

#End result
if count > 0:
    print('Largest number: ', largest)
    print('Count of even numbers: ', even)
    print('Count of odd numbers: ', odd) 