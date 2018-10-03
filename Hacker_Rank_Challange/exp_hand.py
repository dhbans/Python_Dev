T = int(input())
if 0 <= T < 10:
    for x in range(T):
        number = (input())
        a, b = number.split(' ')
        try:
            c=int(a)//int(b)
            print(c)
        except ZeroDivisionError as e:
            print("Error Code:", e)
        except ValueError as e:
            print("Error Code:", e)
