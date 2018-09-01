# This first string operation

s1 = 'Welcome to "core python" learning'
print(s1)

# check the effect of 'r' on special characters
s2 = "This is check of new \n whether success or not"
print(s2)

s3 = r"This is with 'r'\n new line should not be there"
print(s3)

# checking for sub-string and comparision logic with string

str1 = input("Enter the main string: ")
sub_str = input("Enter the sub string to check: ")

if sub_str in str1:
    print('Sub-string is found in main string')
else:
    print('sub-string is not foun in main string')

# comparison of two strings
first_str = 'Let see what happens here'
second_Str = 'Let see what happens here'
third_str = 'Let se what does not happen here'
if first_str == second_Str:
    print('First and second string is same')
if first_str != third_str:
    print('first and third strings are different')


