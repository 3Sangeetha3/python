# Elements can be removed from the List by using the built-in remove()function 
# but an Error arises if the element doesn’t exist in the list. 
# Remove() method only removes one element at a time
# to remove a range of elements, the iterator is used. 
# The remove() method removes the specified item.

# Remove method in List will only remove the first occurrence of the searched element.


List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print("Initial List: ")
print(List)
  
List.remove(5)
List.remove(6)
print("\nList after Removal of two elements: ")
print(List)

# Removing elements from List
# using iterator method
for i in range(1, 5):
    List.remove(i)
print("\nList after Removing a range of elements: ")
print(List)