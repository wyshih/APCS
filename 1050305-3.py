if __name__ == '__main__':
    line = []
    
    segments = int(input())
    
    for i in range(0, segments):
        S, E = input().split(' ')
        if int(S) > int(E):
            print ('Input Error')
            break
        if len(line) < int(E):
            line.extend([0]*(int(E)-len(line)))
        line[int(S):int(E)] = [1]*(int(E)-int(S))
    print (sum(line))
    
