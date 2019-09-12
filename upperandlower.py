def count_case(line):
    low = 0
    up = 0
    for i, ch in enumerate(line):
        if ch.islower():
            low += 1
        elif ch.isupper():
            up += 1
    return low, up

user_input = input("Enter a string: ")

lower, upper = count_case(user_input)

print("Upper case count: ", upper)
print("Lower case count: ", lower)