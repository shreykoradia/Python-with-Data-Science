test_list = ["", "GIT", "", "is", "HACKED", ""]
  
# Printing original list
print ("Original list is : " + str(test_list))
  
# using remove() to
# perform removal
while("" in test_list) :
    test_list.remove("")
      
# Printing modified list 
print ("Modified list is : " + str(test_list))