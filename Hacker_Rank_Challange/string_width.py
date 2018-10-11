def wrap(string, width):
    a = ''
    item = (0 + width-1)
    counter = [0, item]
    item = counter[-1]
    if 0 < len(string) < 1000:
        if 0 < width < len(string):
            for i in range(1,1001):
                item = item + width
                if item <= len(string):
                    counter.append(item)
                if item > len(string):
                    counter.append(len(string))
                    break
            for i in range(0, len(counter)-1):
                if counter[i] == 0:
                    a += (string[counter[i]:counter[i+1] + 1]) + '\n'
                elif counter[i] > 0:
                    a += (string[counter[i] + 1:counter[i+1] + 1]) + '\n'
    return a


if __name__ == '__main__':
    string, width = input() , int(input())
    result = wrap(string, width)
    print(result)
