

class Problem:
    def solve(self, ls_str):
        ls_start, ls_body, ls_end = self.split_parts(ls_str)
        ret, start_chrs = self.helper(ls_start)
        if not ret: return '*'
        ret, end_chrs = self.helper(ls_end)
        if not ret: return '*'
        return ''.join(start_chrs + ls_body + end_chrs[::-1])

    def helper(self, ls_end):
        ls_chr = []
        i = 0
        cur_chr = ''
        while cur_chr is not None:
            ls_chr.append(cur_chr)
            cur_chr = None
            for end in ls_end:
                c = end[i:i+1]
                if c != '':
                    if cur_chr == None:
                        cur_chr = c
                    if c != cur_chr:
                        return False, ls_chr
            i += 1
        return True, ls_chr

    def split_parts(self, ls_str):
        ls_start = []
        ls_body = []
        ls_end = []
        for str_ in ls_str:
            parts = str_.split('*')
            ls_start.append(parts[0])
            ls_body.append(''.join(parts[1: -1]))
            ls_end.append(parts[-1][::-1])
        return ls_start, ls_body, ls_end


if __name__ == "__main__":
    task = Problem()

    T = int(input())
    for i in range(T):
        N = int(input())
        ls_str = [input() for j in range(N)]
        result = task.solve(ls_str)
        print('Case #{}: {}'.format(i+1, result))
    


'''

ACV*C*E
*B*D*
AC*
ACVCBDE


2
5
*CONUTS
*COCONUTS
*OCONUTS
*CONUTS
*S
2
*XZ
*XYZ
'''