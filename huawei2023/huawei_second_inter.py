import bisect

INFINIT = 1e6
DEBUG = False
def debug(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)


def main():
    s = "100011"
    s = "11010"
    s = "1111"
    # 100000
    last_is_1 = None
    rst = []
    for c in s:
        if c == "1":
            if last_is_1 is None:
                last_is_1 = len(rst)
                # print(last_is_1)
                rst.append(c)
            else:
                if last_is_1 > 0:
                    rst[last_is_1-1] = '1'
                    rst[last_is_1] = '0'
                    rst.append("0")
                    last_is_1 = None
                else:
                    rst = ["1"] + ["0"] * len(s)
                    break
        else:
            last_is_1 = None
            rst.append(c)
            
    print(''.join(rst))
    

while True:
    try:
        main()
        break
    except EOFError:
        break