# This program is understand
"""
string.count(substring, startofindex , endofindex)
it return number of count of substring in string

"""

str1 = input('enter the main string: ')
str2 = input('enter the sub string: ')
count = str1.count(str2,0 , 12)
print(' The number of substring in string is {}'.format(count))


# Program to check immutable


a = 'check'
b = 'hello'
print(id(a))
print(id(b))
a=b
print(a)
print(b)
print(id(b))
print(id(a))


# split function of string
"""

syntax:
string.split('Delimiter')
empty delimiter gives: ValueError: empty separator

"""
string1 = 'a b c d e f g h k'
list1 = string1.split(' ')
print(list1)

# Join function to make list or different character to string.
"""
syntax:
"delimiter".join(list)

"""
list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'k']
print(' '.join(list2))


