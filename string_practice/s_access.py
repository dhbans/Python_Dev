# this program is to access string element for start and last

s1 = 'core python'
print(len(s1))
for i in range(len(s1)):
    print(s1[i], end=' ')

print()
i = -1
while i >= -(len(s1)):
    print(s1[i], end=' ')
    i -= 1

# Using other way to access from last
print()
i = 1
while i <= len(s1):
    print(s1[-i], end=' ')
    i += 1

# using slicing

print('\n', s1[::], end='\n')
print(s1[::-1], end=' ')
