#Number of seconds in a year, I'll use this to help me calculate the deaths and births per year. 365 days * 86,400 seconds.
seconds = 31536000.0
#This is the current population in the USA according to the assignment.
CurrentPop = 307357870.0

years = int(input('Years: '))

#Death every 13 seconds. Outcome per year. 
deaths = seconds/13

#Birth every 7 seconds. Outcome per year. 
births = seconds/7

#New immigrant every 35 seconds. Outcome per year. 
immigrants = seconds/35

#Estimated population
if years >= 0:
    EstPop = CurrentPop + (years*births) + (years*immigrants) - (years*deaths)
    print('New population after',int(years),'years is',int(EstPop))
else:
    print('Invalid input!')
