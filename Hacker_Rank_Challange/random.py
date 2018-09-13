list1 = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
#list1 = [['b', 23.0], ['a', 23.0]]

list1.sort(key=lambda x:x[1])
print(list1)
