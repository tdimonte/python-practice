'''
Arrays
- fixed size, locates based on index
- contigous (store info in adjoining blocks of memory)
- "typed" array data strucutre only allows specifict data type elements
- O(1) time complexity
'''

#list - datatype, can be declared w []
#list - mutable, dynamic array
arr = ["one", "two", "three"]
print(arr[0])

print(arr)

#lists are mutable
arr[1] = "hello"
print(arr)

#lists can hold arbitrary data types
arr.append(23)
print(arr)