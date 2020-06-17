def solve_quad(a,b,c):
    d = (b**2-4*a*c)**(1/2)
    return max((-b + d) / (2 * a), (-b - d) / (2 * a))

def ceil(fl):
    return int(fl) + (1 if fl-int(fl) else 0)

def bigbang(L, R):
    x = solve_quad(1-2*(L>R), 1-2*(L>R), 2*(L-R))
    return int(x) if L>R else ceil(x)

if __name__ == '__main__':
    num_cases = int(input())
    for i in range(1, num_cases+1):
        L, R = map(int, input().split())
        
        start = bigbang(L, R)
        func = lambda a, b : a - (a>b)*start*(start+1)/2 
        L = func(L, R)
        R = func(R, L)
        n_L = int(solve_quad(1, start, -L))
        n_R = int(solve_quad(1, (start+1), -R))
        n = start + n_L + n_R
        l = int(L - n_L*(start+n_L))
        r = int(R - n_R*(start+n_R+1))

        print('Case #{}: {} {} {}'.format(i,n,l,r))
