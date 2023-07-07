import bisect

INFINIT = 1e6
DEBUG = False
def debug(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)

VALUES = [0, "A"] + [str(i) for i in range(2, 11)] + ["J", "Q", "K"]

OP_DICT = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x // y
}

def main():
    inp = input().strip().split(" ")
    try:
        values = [VALUES.index(x) for x in inp]
    except:
        print("ERROR")
        return

    def dfs(rands, ops, candidates:list):
        if len(candidates) == 0:
            output = values[rands[0]]
            for i in range(len(ops)):
                output = OP_DICT[ops[i]](output, values[rands[i+1]])
            if output == 24:
                algebra_seq = f"{inp[rands[0]]}"
                for i in range(len(ops)):
                    algebra_seq+=f"{ops[i]}{inp[rands[i+1]]}"
                # if algebra_seq == 'K*A/2*4':
                #     import pdb; pdb.set_trace()
                return [algebra_seq]
            else:
                return None
        rst = []
        for c in candidates:
            for op in ["+", "-", "*", "/"]:
                ops.append(op)
                rands.append(c)
                _candidates = candidates.copy()
                _candidates.remove(c)
                ret = dfs(rands, ops, _candidates)
                if ret is not None:
                    rst += ret
                rands.pop(-1)
                ops.pop(-1)
        return rst
    
    candidates = set(range(len(values)))
    rst = []
    for op in ["+", "*"]:
        for i in range(len(values)-1):
            candidates.remove(i)
            for j in range(i+1, len(values)):
                candidates.remove(j)
                ret = dfs([i, j], [op], candidates)
                if ret is not None:
                    rst += ret
                candidates.add(j)
            candidates.add(i)
    
    for op in ["-", "/"]:
        for i in range(len(values)):
            candidates.remove(i)
            for j in range(len(values)):
                if i == j:
                    continue
                # if i ==2 and j == 3:
                #     import pdb; pdb.set_trace()
                candidates.remove(j)
                ret = dfs([i, j], [op], candidates)
                if ret is not None:
                    rst += ret
                candidates.add(j)
            candidates.add(i)
    
    if len(rst) == 0:
        print("NONE")
    else:
        print(rst[0])
    

while True:
    try:
        main()
    except EOFError:
        break