import bisect

INFINIT = 1e6
DEBUG = False
def debug(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)


def main():
    s1 = "999999999"
    s2 = "987654321"
    all_sum = []
    max_len = 0
    for i, b in enumerate(s2[::-1]):
        sum = [0] * i
        residual = 0
        for a in s1[::-1]:
            rst = int(b) * int(a) + residual
            sum.append(rst % 10)
            residual = rst // 10
        if residual > 0:
            sum.append(residual)
        all_sum.append(sum)
        print(sum)
        max_len = len(sum)
    
    residual = 0
    ret = []
    print(all_sum)
    for j in range(max_len):
        k = residual
        for sum in all_sum:
            if j < len(sum):
                k += sum[j]
        ret.append(k % 10)
        residual = k // 10
    print("".join([str(x) for x in ret[::-1]]))

while True:
    try:
        main()
        break
    except EOFError:
        break