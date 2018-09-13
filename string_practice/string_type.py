# this program is to check the type of string

user_string = input('please enter the string: ')

if user_string.isupper()and (user_string.isalnum() == 1 or user_string.isalnum() == 0)\
        and (user_string.isalpha() == 1 or user_string.isalpha() == 0) \
        and user_string.lower() == 0:
    print('The string given by user is all upper case string')

elif user_string.islower()and user_string.isdigit() == 0 and \
        (user_string.isalnum() == 1 or user_string.isalnum() == 0)\
        and user_string.isalpha() == 1 or user_string.isalpha() == 0 and user_string.isupper() == 0 :
    print('the string is all lower case string')

elif user_string.istitle() and user_string.isalnum() == 1 and user_string.isalpha() == 1 and \
        user_string.isupper() == 0 and user_string.islower() ==0:
    print('The string is of tittle type')

elif user_string.isdigit() and user_string.isalnum() == 1:
    print('The string given by user is digits')

elif user_string.isalnum() and user_string.islower() == 0 and user_string.isupper() == 0 and\
        user_string.istitle()==0 and user_string.isdigit() == 0:
    print('The string given by user is alpha numeric')

