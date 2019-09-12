def palinCheck(string):
    
    newString = ''

    for ch in string:
        if string.isalpha():
            newString += ch

    if newString == newString[::-1]:
        return True
    else:
        return False
        
        
        

in_str = input("Enter a string: ")
checker = palinCheck(in_str)

if checker:
    print("\""+in_str+"\" is a palindrome.")

else:
    print("\""+in_str+"\" is not a palindrome.")