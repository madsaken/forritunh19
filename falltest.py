my_string = "x" *10

def insert(x):
    new_my_string = my_string[:x-1] + my_string[x].replace("x","o") + my_string[x:]
    return new_my_string



position = int(input("Input a position between 1 and 10: "))

print(insert(position))
print("l - for moving left")
print("r - for moving right")
print("Any other letter for quitting")



while position:

    my_choice = input("Input your choice: ")

    if (position >= 1 or position <= 10):
        if my_choice == "l":
            position-=1
            print(insert(position))
        elif my_choice == "r":
            position+=1
            print(insert(position))