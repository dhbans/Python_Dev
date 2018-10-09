from collections import deque

d = deque()
operation = ''
value = ''
number = int(input())
for i in range(0,number):
    if 0 < number <= 100:
        user_input = input()
        if ' ' in user_input:
            operation, value = user_input.split(' ')
        else:
            operation = user_input
        if operation == 'append':
            d.append(value)
        elif operation == 'pop':
            d.pop()
        elif operation == 'popleft':
            d.popleft()
        elif operation == 'appendleft':
            d.appendleft(value)

for item in d:
    print(item,end=' ')

