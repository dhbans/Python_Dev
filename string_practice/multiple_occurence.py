# This is program to find multiple occurrence of sub_String in string

string1 = input('enter the main string: ')
string2 = input('enter the sub_String value: ')

flag = False
index = 0
while index <= len(string1):
    result = string1.find(string2, index, len(string1))
    if result != -1:
        print('string is found at ', result, result+len(string2))
        position = result + 1
        index = position
        flag = True
    else:
        index += 1
if flag == 0:
        print('String is not found')
