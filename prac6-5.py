str1 = "English = 78 Science = 83 Math = 68 History = 65"
str2 = str1.split(' ')
nums = 0
count= 0
for i in str2:
    if i.isdigit():
        nums+= int(i)
        count+=1
        
print(nums)
print(nums/count)   