'''
Tuples
- unlike lists, tuple objects are immutable
- elements cannot be added or removed dynamically
- elements must be defined at creation
- arbitrary data types, data is less tightly packed then typed array
'''

#tuple - datatype, can be declared with ()
arr = ("one", "two", "three")
print(arr[0])

print(arr)

#tuples are immutable
#arr[1] = "hello"
print(arr)

#tuples can hold arbitrary data types
arr = arr + (23,)
print(arr)