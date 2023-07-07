import bisect

INFINIT = 1e6
DEBUG = False
def debug(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)

UNITS = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖"]
UNIT1e1 = [None, "", "拾", "佰", "仟"]
UNIT_FRAC = ["角", "分"]
UNIT1e4 = ["", "万", "亿"]

def main():
    inp = input().strip()
    if "." in inp:
        whole, fraction = inp.split(".")
    else:
        whole, fraction = inp, ""

    output = ""
    whole_level = len(whole) // 4
    assert whole_level < len(UNIT1e4)
    exit_zero = False
    while whole_level >= 0:
        if whole_level == 0:
            inner_whole = whole[-4:]
        else:
            inner_whole = whole[-(whole_level * 4 + 4):-(whole_level * 4)]
        
        level = len(inner_whole)
        local_output = ""
        pre_zero = False
        while level >= 1:
            v = int(inner_whole[-level])
            if v == 0:
                if not pre_zero and exit_zero:
                    local_output += f"{UNITS[v]}"
                else:
                    pass
                pre_zero = True
                exit_zero = True
            elif v == 1 and level == 2:
                local_output += f"{UNIT1e1[level]}"
            else:
                local_output += f"{UNITS[v]}{UNIT1e1[level]}"
                pre_zero = False
            level -= 1
        # print(local_output)
        output += f"{local_output}{UNIT1e4[whole_level]}"
        whole_level -= 1
    
    if len(output) > 0:
        output += "元"

    if len(fraction) == 0 or int(fraction) == 0:
        output += "整"
    else:
        for i, c in enumerate(fraction):
            v = int(c)
            if v != 0:
                output += f"{UNITS[v]}{UNIT_FRAC[i]}"
    print("人民币" + output)

while True:
    try:
        main()
    except EOFError:
        break