count = 0  #A counter.
deci = 0   #Short for decimal.


for j in range(10,100):    #The for loop will begin with 10 and go up to 100.

    for r in range(1,10):           
        deci = j-r                  #I'll use this to check for any possible splits
        if deci % 10 == 0:          #If 'j' - 'r' equals a power of 10 then we have to remove one zero from it. 
            deci = deci/10          #For example: 23 will become 20 then 2. 'r' remembers the 3. 23 split into 2 and 3.
            if (deci+r)**2 == j:    #If the calculated number 'deci' + 'r' squared equals the original 'j',
                print(j)            #then it will be printed.
    deci = 0


for i in range(1,100):      #All positive numbers less than zero

    for q in range(1, i+1):
        if i % q == 0:      #A checker for divisors
            count += 1
    if count == 10:         #If the count equals 10, then that particular number has 10 divisors
        print(i)

    count = 0 
