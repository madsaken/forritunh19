decimal = int(input("Enter a decimal number and the outcome will be in binary: ")) # Do not change this line
rem = decimal
binary = ""
for i in range(decimal,-1,-1):
    if 2**i <= rem:
        rem = rem - (2**i)
        binary = binary + "1"
    elif binary != "":
        binary = binary + "0"
        
print(binary)