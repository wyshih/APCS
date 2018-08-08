if __name__ == '__main__':
    line = []   #set a list to record segments if occupied the value of that index is set to 1
    
    segments = int(input())
    
    for i in range(0, segments):
        S, E = input().split(' ')
        if int(S) > int(E):
            print ('Input Error')
            break
        if len(line) < int(E):  #if the new segment is longer than record list then extend the record
            line.extend([0]*(int(E)-len(line)))
        line[int(S):int(E)] = [1]*(int(E)-int(S))   #set the range of segment in reocrd list to 1
    print (sum(line))   #sum all values in record list and print the value which is the length of all segments
    
