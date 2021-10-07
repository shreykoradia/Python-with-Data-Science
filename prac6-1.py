str1 = 'Ault'
str2 = 'Kelly'
l = len(str1)//2
str3 = str1[0:l] + str2 + str1[l::] 
print(str3)