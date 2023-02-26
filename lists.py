#creating an empty list
List = []
print("Blank List: ",List)
print(List)

#creating a list with strings and integers
mydata =["Sangeetha", "Btech", "CSE", 17, 17] 
#printing the list
print(mydata)
#indexing of a list
print(mydata[0]) # accessing an elemnet from the list
print(mydata[2])
print(mydata[3])
print(mydata[4]) #lists can have duplicate values also

# nesting of a list 
mydata1 =[["Sangeetha", "Btech", "CSE", 17, 17], 0, 12]
print(mydata1[0][0]) #accesssing the element from the multi dimensional list using index
print(mydata1[0][1]) 
print(mydata1[1])
#negative indexing
print(mydata1[-1])
print(mydata1[-3])
print(mydata1[-3][-1])

