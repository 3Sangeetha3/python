list_arr = [1, 2, 3, 2, 1]
list_string = list("geetha")
 
# store a copy of list
list2 = list_arr.copy()
list3 = list_string.copy() 
 
# reverse the list
list2.reverse()
list3.reverse()
 
# compare reversed and original list
if list_arr == list2:
    print(list_arr, ": Palindrome")
else:
    print(list_arr, ": Not Palindrome")
 
# compare reversed and original list
if list_string == list3:
    print(list_string, ": Palindrome")
else:
    print(list_string, ": Not Palindrome")