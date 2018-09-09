# to check string start with and end with

string1 = input('please enter the string: ')
sub_string = input('enter the sub string with which need to check start: ')
if string1.startswith(sub_string):
    print('string start with given sub-string')
elif string1.endswith(sub_string):
    print('string end with given sub-string')
else:
    print('string is start and end with random strings')