

def lcs(X , Y): 
    m = len(X) 
    n = len(Y) 
    L = [[None]*(n+1) for i in range(m+1)] 
 
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1]) 
  
    return L[m][n], L


def solve(C, J):
    C_idx = []
    J_idx = []
    common_str = ''
    L, bit_map = lcs(C, J)
    
    m = len(C) 
    n = len(J)

    while L > 0:
        if C[m-1] == J[n-1]:
            common_str = C[m-1] + common_str
            C_idx.append(m-1)
            J_idx.append(n-1)
            m -= 1
            n -= 1
            L -= 1
        elif bit_map[m-1][n] > bit_map[m][n-1]:
            m -= 1
        else: n -= 1

    res = ''
    turn = False
    pre_c = 0
    pre_j = 0
    C_idx = C_idx[::-1]
    J_idx = J_idx[::-1]
    C_idx.append(len(C))
    J_idx.append(len(J))
    for c , j in zip(C_idx, J_idx):
        c_part = C[pre_c: c]
        j_part = J[pre_j: j]
        pre_c = c+1
        pre_j = j+1
        len_max = max(len(c_part), len(j_part))
        for i in range(len_max):
            if turn:
                turn = False
                if i < len(c_part):
                    res += c_part[i]
            else:
                turn = True
                if i < len(j_part):
                    res += j_part[i]
        
        if c < len(C):
            res += C[c]
    return res
    

if __name__ == "__main__":
    n_cases = int(input())
    for i in range(n_cases):
        C, J = input().split()
        N = solve(C, J)
        print('Case #{}: {}'.format(i+1, N))
        
    