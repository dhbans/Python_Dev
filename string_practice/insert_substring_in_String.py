# this program to insert string in particular index of string.

m_string = input('Please enter Main string: ')
s_string = input('Please enter sub string need to insert in main string: ')
index = input('please enter the Index where need to be inserted: ')

list1 = []
for s in m_string:
    list1.append(s)
list1.insert(int(index),s_string)
print(''.join(list1))
print(list1.sort())
print(list1)