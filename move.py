Left = 1
Right = 10

def moverFunction(x):
    #This function makes a new board.
    newLocation = x
    newX_left = newLocation-Left
    newX_right = Right-newLocation
    newBoard = "x"*newX_left + "o" + "x"*newX_right
    print(newBoard)

 
        
ans = 'l'
placement = int(input("Input a position between 1 and 10: "))
x_right = Right-placement                   #Math to determine where to place the 'o'
x_left = placement-Left                     # ---||---
board = "x"*x_left + "o" + "x"*x_right      #Construction of the board.
print(board)
print("l - for moving left")
print("r - for moving right")
print("Any other letter for quitting")

while ans == 'l' or ans == 'r':
    ans = input("Input your choice: ")

    if ans == 'l':                      #Moves the 'o' one place to the left if the user entered 'l'
        if placement != 1:              #If the 'o' is on the far left, it won't change the placement
            placement = placement-1     #and will call on 'moverFunction' to print the board.
            moverFunction(placement)
        else:
            moverFunction(placement)

    elif ans == 'r':                    #This elif does the same as the one above it except it handles the
        if placement != 10:             #right movement.
            placement = placement+1
            moverFunction(placement)
        else:
            moverFunction(placement)

    else:
        moverFunction(placement)        #When the user enters anything other than 'l' or 'r' the current board
                                        #will print and the session will end.