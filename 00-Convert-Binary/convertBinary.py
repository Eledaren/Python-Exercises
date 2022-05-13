def binaryToDecimal(binary):
    decimal = 0
    m = 1
    
    for digit in binary:
        digit = int(digit)
        decimal += int(digit) * m
        m *= 2
    return decimal

def decimalToOctal(decimal):
    octal = 0
    m = 1
    
    while (decimal != 0):
        octal += decimal % 8 * m
        decimal //= 8
        m *= 10
    return octal

binary = input("Enter a binary number: ")
choose = input("Enter 1 if you want to convert to decimal or 2 for octal: ")
decimal = binaryToDecimal(binary)
octal = decimalToOctal(decimal)

if choose == "1":
    print(decimal)
elif choose == "2":    
    print(octal)
else:
    print("Input Error")