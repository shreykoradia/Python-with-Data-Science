s1 = "Yng"

s2 = "PYnative"

res = True
for i in s1:
    if i in s2:
        res = True
    else:
        res = False
        break
print(res)