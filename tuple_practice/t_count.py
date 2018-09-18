# this section will cover tuple declaration

# empty tuple we can declare but not use case as we can't add any data in it.
data = ()
print(type(data))

# tuple with single value without ","
data_root = ('root')
print(type(data_root))

data_number = (1)
print((type(data_number)))

""" 
in above to single element declaration we can see that type is str and int respectively to over come this 
we need to pass ',' in between
"""

data_root = ('root',)
print(type(data_root))

data_number = (1,)
print((type(data_number)))



# this is to check count of element in tuple
"""
tuple.count('string)
return no. of string.
return 0 if not found


tuple.index(element, start, end )
return index of first occurrence of element

raise value error exception if not present in tuple
"""

tuple1 = ('a', 'a', 'c', 1, 2, 3, 4, 5, 1, 1, 2, 2)
print(tuple1.count('z'))
print(tuple1.count('m'))
print(tuple1.index('m',0,2))


