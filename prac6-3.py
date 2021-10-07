chars = 0
digits = 0
symbol = 0

str1 = "P@#yn26at^&i5ve"

for i in str1:
    if i.islower() or i.isupper():
        chars+=1
    elif i.isnumeric():
        digits+=1
    else:
        symbol+=1
print('chars :', chars)
print('digits :', digits)
print('symbol :', symbol)
