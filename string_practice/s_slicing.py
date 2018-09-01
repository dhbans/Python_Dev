# this Program is to understand slicing of a string

string1 = 'This is practice session fo python programing'
print(string1[::3])
print(string1[1::1]) # Positive index left to right
print(string1[1::-1]) # Negative index right to left

print(string1[-4:])
print(string1[-4::-1])

# Repeating of string
print(string1*3,end="\n")
s1 = 'dhruv'
s2 = 'bansal'
s3 = s1 + s2
print(s3)