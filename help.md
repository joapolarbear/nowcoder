
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
    b = b.rjust(len(a),"0")
```