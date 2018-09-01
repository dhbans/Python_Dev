# this Program is practice occurrence of sub-string in string.

"""
Some useful points:

syntax: string.find/index/rfind/rindex(substring, beginning , ending )

string.find(): Find from left to right. return -1 if not found
string.index(): Find from left to right. return ValueError if not found
string.rfind(): Find from right to left
string.rindex(): Find from right to left .

"""
#  example of find
string1 = input('Enter main string: ')
sub_String1 = input('Enter sub_String: ')


result = string1.find(sub_String1, 0, len(string1))
if result == -1:
    print('Substring {} is not found in string {}'.format(sub_String1 , string1))
else:
    print('range of index is ({},{})'.format(result,result+len(sub_String1)))


result = string1.index(sub_String1, 0, len(string1))
if result == -1:
    print('Substring {} is not found in string {}'.format(sub_String1 , string1))
else:
    print('range of index is ({},{})'.format(result,result+len(sub_String1)))


