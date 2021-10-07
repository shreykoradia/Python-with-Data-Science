str1 = 'PyNoTion'
s = ''
S = ''
for i in str1:
    if i.islower():
        s+=i
    elif i.isupper():
        S+=i
print(s+S)