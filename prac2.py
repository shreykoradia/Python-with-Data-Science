# Python id() function example
l1 = [1,2,3,4]
l2 = [1,2,3,4]
l3 = [3,5,6,7]
# Calling function
id1 = id(l1)
id2 = id(l2)
id3 = id(l3)

# printing of id of list 1
print(id(l1))
print(id(l2))
print(id(l3))
# Displaying result
print((l1==l2),(l1==l3))
# Objects with the same values can have different ids
print((id1==id2),(id1==id3))
# l1 and l2 returns True, while id1 and id2 returns False


# my output before running is :
# true false
#false false