#append() method only works for the addition of elements at the end of the List
#append() which takes only one argument

#creating an empty list
List = []
print("Initial blank List: ")
print(List)

#adding an elements to the list using append
List.append(7)
List.append(8)
List.append(9)
print("\nList after Addition of Three elements: ")
print(List)
  
for i in range(1, 4):
    List.append(i)
print("\nList after Addition of elements from 1-3: ")
print(List)
  
#adding a tuple to the list 
List.append((5, 6))
print("\nList after Addition of a Tuple: ")
print(List)

#addding a list ot the list
List2 = ['Hello', 'Sangeetha']
List.append(List2)
print("\nList after Addition of a List: ")
print(List)
