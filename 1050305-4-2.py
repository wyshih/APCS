#another solution for 4th problem
def matrix_mul(adj, new_adj, n):    # matrix multiplication
    matrix = [[0 for j in range(n)] for i in range(0, n)]
    for i in range(n):
        row = adj[i]
        for j in range(n):
            col = [new_adj[m][j] for m in range(n)]
            temp = 0
            for g in range(n):
                temp += row[g]*col[g]
            matrix[i][j] = temp
    return matrix
def check_new_arrival(adj): # check whether a new path is created, if there is 1 in the new matrix
    for i in range(n):
        for j in range(n):
            if adj[i][j] == 1:
                return 1
    return 0
if __name__ == '__main__':
    
    n = int(input())
    blood = [[0 for j in range(n)] for i in range(0, n)]

    for i in range(0, n-1):
        P, C = input().split(' ')
        P = int(P)
        C = int(C)
        blood[P][C] = 1     # if there is connection between C and P, set [P][C] = 1
        blood[C][P] = 1     # since the connection is undirected, the connection is mutual

    flag = 1
    step = 1
    a = blood
    while(flag):            # find the last new connection and count the steps
        a = matrix_mul(blood, a, n)
        flag = check_new_arrival(a)
        if flag == 1:
            step += 1
    print (step)
        
