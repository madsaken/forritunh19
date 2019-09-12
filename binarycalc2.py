my_int = int(input('Give me an int >= 0: '))

quotient = my_int
bin_str = ""

while quotient >= 1:

    if quotient % 2 == 0:
        bin_str = bin_str+"0"
    else:
        bin_str = bin_str+"1"
    quotient = int(quotient/2)

if quotient == 0:
    bin_str = bin_str+"0"

print("The binary of", my_int, "is", bin_str[::-1])