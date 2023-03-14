# extend(), this method is used to add multiple elements at the same time at the end of the list.

# append() and extend() methods can only add elements at the end.

List = [1, 2, 3, 4]
print("Initial List: ")
print(List)

  
# Addition of multiple elements to the List at the end (using Extend Method)
List.extend([8, 'Hello', 'Sangeetha'])
print("\nList after performing Extend Operation: ")
print(List)
