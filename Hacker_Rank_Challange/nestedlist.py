N = int(input())
list1 = []
name_list = []
score_list = []
if N >= 2 and N <= 5:
    for i in range(0,N):
        name = input()
        score = float(input())
        name_list.append(name)
        score_list.append(score)


# hera ziping the two list to make 1 nested list
for s,n in zip(name_list,score_list):
    list1.append([s,n])
list1.sort(key=lambda x: x[1])
dict1 = {}

if len(list1) == 2:
            dict1[list1[1][0]] = list1[1][1]

if len(list1) > 2:
    set_list = []
    for i in range(0,len(list1)):
        set_list.append(list1[i][1])
        score_list = list(set(set_list))
        score_list.sort()
    for i in range(0,len(list1)):
        if list1[i][1] == score_list[1]:
                dict1[list1[i][0]] = list1[i][1]

list2 = list(dict1)
list2.sort()
for i in list2:
    print(i)