# `bisect` library
bisect.bisect_left(a, x, lo=0, hi=len(a), *, key=None)
The returned insertion point i partitions the array a into two halves so that 
- all(val < x for val in a[lo : i]) for the left side and
- all(val >= x for val in a[i : hi]) for the right side.

# 注意eval() 函数不能判断开头是0的数字
# Note the spelling of forty, fifteen, fifty
# 倒序 搜索：`for i in range(a, 0, -1):`
# 有while 的地方就得检查是否有死循环的可能

```bash
>>> l.is
l.isalnum(      l.isascii(      l.isdigit(      l.islower(      l.isprintable(  l.istitle(     
l.isalpha(      l.isdecimal(    l.isidentifier( l.isnumeric(    l.isspace(      l.isupper(  

__需要分别考虑字符串为空、通配符为空的情形__
```
# 动态规划建表多设一行的时候注意 `range(1 + len(s))`, 别忘了`+1`，后续填表的时候 `for i in range(1, 1+len(s))`


# Valid IP Address
```Python
def valid_ip(ip_split):
    if len(ip_split) != 4:
        return False
    for idx, _ip in enumerate(ip_split):
        if len(_ip) == 0 or not _ip.isdigit():
            return False
        ip_value = eval(_ip)
        if (ip_value > 0 and _ip[0] == "0") or ip_value > 255:
            return False
    return True

valid_ip(ip.split("."))
```

## IP to int
```python
def ip2int(ip_split):
    return int(''.join([bin(int(m))[2:].rjust(8, '0') for m in ip_split]), base=2)
```
## Check if a mask is valid
```python
### check the mask
mask_bin = ''.join([bin(int(m))[2:].rjust(8, '0') for m in mask])
first_zero_idx = -1
if mask_bin[0] == '0':
    valid = False
else:
    for idx, m in enumerate(mask_bin):
        if m == '0':
            if first_zero_idx < 0:
                first_zero_idx = idx
            else:
                pass
        elif first_zero_idx >= 0:
            valid = False
            break
    if valid and first_zero_idx < 0:
        valid = False
```

# Python String `rjust()` Method
Return a 20 characters long, right justified version of the word "banana":
```Python
if len(b) <= len(a):
    b = b.rjust(len(a), "0")
```

# pack problem
```Python
N, V = map(int, input().split())  # 物品数， 背包容量

v = [0] * (N + 1)  # 体积 索引从1开始到n
w = [0] * (N + 1)  # 价值 索引从1开始到n

for i in range(1, N + 1):
    v[i], w[i] = map(int, input().split())

f = [0 for i in range(V+1)]  # 初始化全0

for i in range(1, N + 1):
    for j in range(V,v[i]-1,-1):
            f[j] = max(f[j], f[j - v[i]] + w[i])

print(f[V])

