n = int(input("Enter the length of the sequence: ")) # Do not change this line

first_int = 1
sec_int = 2
third_int = 3
storage = 0

print(first_int)
print(sec_int)
print(third_int)

for i in range(3,n):

    storage = first_int + sec_int + third_int
    first_int = sec_int
    sec_int = third_int
    third_int = storage
    print(storage)