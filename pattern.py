n = int(input("Number of stars: "))

Stars = '*' #'Stars' is a string that eventually prints the stars.
counter = 0 #'Counter' will count the number of circles the loop has run.

if n >= 0: #'n' can't be less than 0.
    while counter < n:
        print(Stars)
        Stars = Stars + '*'
        counter += 1