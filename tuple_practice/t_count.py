# this is to check count of element in tuple
"""
tuple.count('string)
return no. of string.
return 0 if not found


tuple.index(element)
return index of first occurrence of element

raise value error exception if not present in tuple
"""

tuple1 = ('a', 'a', 'c', 1, 2, 3, 4, 5, 1, 1, 2, 2)
print(tuple1.count('z'))
print(tuple1.count(1))
print(tuple1.index('k'))