def turn(R, M, matrix):     #turn matrix
    result = [[0]*R for i in range(0, M)]
    #print result
    for i in range(0, R):
        for j in range(0, M):
            result[j][R-i-1] = matrix[i][j]
    #print result
    return result
'''
original    after turn      new index

00 01       20 10 00         00 01 02
10 11   ->  21 11 01   <-->  10 11 12
20 21

the original columns become row, and the order of original rows are reversed to become new columns

'''
def reverse(R, M, matrix):
    result = [[0]*M for i in range(0, R)]
    for i in range(0, R):
        for j in range(0, M):
            result[R-i-1][j] = matrix[i][j]
    #print result
    return result

'''
original    after reverse

00 01       20 21       
10 11   ->  10 11     
20 21       00 01

the columns are not changed, but the order of rows are reversed
'''
if __name__ == '__main__':
    R, M, C = input().split(' ')
    R = int(R)
    M = int(M)
    C = int(C)
    if R < 1 or M < 1 or C< 1 or R > 10 or M > 10 or C > 10:
        print ('Redefine Your Matrix.')
        #return 0
    matrix = []
    while True:
        raw_line = input()
        
        if raw_line == '' or raw_line == None:
            break
        line = [int(i) for i in raw_line.split()]
        if len(line) != M:
            print ('The number of columns is not matched.')
            break
        matrix.append(line)
        if len(matrix) == R:
            break
    if len(matrix) != R:
        print ('The number of rows is not matched.')
        #return 0
    command = [int(i) for i in input().split()]
    if len(command) != C:
        print ('The number of commands is not matched.')
        #return 0
    for i in command:
        if i == 0:
            matrix = turn(len(matrix), len(matrix[0]), matrix)
        elif i == 1:
            matrix = reverse(len(matrix), len(matrix[0]), matrix)
    print ("===========Result===============")
    print (len(matrix), len(matrix[0]))
    for i in range(0, len(matrix)):
        print (''.join(str(p)+' ' for p in matrix[i])[:-1])
