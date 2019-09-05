first = int(input('First: '))
step = int(input('Step: '))

summary = 0

if step > 0: #If step is less than 0, the loop will never close.
    for i in range(first, 101, step): #I use 101 because that is the highset possible count,
                                      #even though summary will break it before.
        if summary >= 100:
            break       #Listener for 'Summary' more or equal to 100 to break the loop.
        print(i, end=' ')
        summary = summary + i
    print('')

if step == 0:     #This loop will take care of the Range(), arg 3 problem. Step must not be 0.
    while summary < 100:
        print(first, end=' ')
        summary += first
    print('')


print('Sum of series: ', summary)