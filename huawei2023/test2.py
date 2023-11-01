import bisect

INFINIT = 1e6
DEBUG = False
def debug(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)


    
def main():
    R, C = list(map(int, input().split(" ")))
    array = [[] for _ in range(R)]
    for i in range(R):
        array[i] = list(map(int, input().split(" ")))
        debug(array[i])
        
    N = R * C
    def serial(r, c):
        return r * C + c
    def deserial(n):
        r = n // C
        c = n % C
        return r, c
    table = [None for _ in range(N)]
    
    def longest_decrease_path(r, c, history):
        # nonlocal table
        n = serial(r, c)
        if n in history:
            return 0
        if table[n] is not None:
            return table[n]
        
        longest_len = 1
        if r > 0 and array[r][c] > array[r-1][c]:
            longest_len = max(longest_len,
                1 + longest_decrease_path(r-1, c, history+[n]))
        
        if r < R-1 and array[r][c] > array[r+1][c]:
            longest_len = max(longest_len,
                1 + longest_decrease_path(r+1, c, history+[n]))
        
        if c > 0 and array[r][c] > array[r][c-1]:
            longest_len = max(longest_len,
                1 + longest_decrease_path(r, c-1, history+[n]))
        
        if c < C-1 and array[r][c] > array[r][c+1]:
            longest_len = max(longest_len,
                1 + longest_decrease_path(r, c+1, history+[n]))
        
        table[n] = longest_len
        return longest_len
        
    longest_len = 0
    for r in range(R):
        for c in range(C):
            longest_len = max(longest_len,
                longest_decrease_path(r, c, []))
    print(longest_len)

while True:
    try:
        main()
    except EOFError:
        break