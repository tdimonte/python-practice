'''
Dictionaries
- arbitrary # of objects
- identified by a unique dictionary key
- also called maps/hashmaps/lookuptables/associativearrays
- lookup, insertion, deletion of obj w key
- keys are hashable type (they do not change and can be compared "__eq__")
- O(1) time complexity (for lookup, insert, update and delete)
'''

#dict - datatype, can be declared with {}

phonebook = {
    "tom": 6300,
    "vicky": 9104,
    "ale": 7086
}

print(phonebook["vicky"])

squares = {x: x * x for x in range(6)}
print(squares)


