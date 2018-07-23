#second Problem 1
def judge(length):
    flag = 0
    length.sort()
    if length[0] + length[1]  <= length[2]:
        return 'No'
    elif pow(length[2], 2) == pow(length[0], 2) + pow(length[1], 2):
        return 'Right'
    elif pow(length[2], 2) > pow(length[0], 2) + pow(length[1], 2):
        return 'Obtuse'
    elif pow(length[2], 2) < pow(length[0], 2) + pow(length[1], 2):
        return 'Acute'
if __name__ == '__main__':
    a, b, c = input().split(' ')
    a = int(a)
    b = int(b)
    c = int(c)
    length = []
    if a < 30001 and a > 0 and b < 30001 and b > 0 and c < 30001 and c > 0:
        length.append(a)
        length.append(b)
        length.append(c)
        print (judge(length))
    else:
        print ("Wrong length!")
