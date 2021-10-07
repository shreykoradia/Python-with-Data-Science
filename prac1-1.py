def checkValidity(a, b, c):
     
    # check condition for triangle 
    if (a + b <= c) or (a + c <= b) or (b + c <= a) :
        return False
    else:
        return True       

len1 = float(input("Enter the valid number1:"))
len2 = float(input("Enter the valid number2:"))
len3 = float(input("Enter the valid number3:"))
if checkValidity(len1, len2, len3):
    print("Valid")
else:
    print("Invalid")