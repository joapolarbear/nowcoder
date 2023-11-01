import bisect

INFINIT = 1e6
DEBUG = False
def debug(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)

def main():
    N = int(input())
    M = int(input())
    debug(N, M)
    cards = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        cards[i] = list(map(int, input().split(" ")))
        debug(cards[i])
    
    table = []
    left = N
    round = 0
    while left > 1:
        for i in range(1, N+1):
            if len(cards[i]) == 0:
                continue
            card = cards[i].pop(0)
            win = False
            for j in range(len(table)):
                if table[j] == card:
                    win_cards = table[j:] + [card]
                    table = table[:j]
                    cards[i] = cards[i] + win_cards[::-1]
                    debug(f"win, {i} with {cards[i]}")
                    win = True
                    break
            if not win:
                table.append(card)
            debug(f"round {round}, {i}->{card}, table {table[::-1]}")
            if len(cards[i]) == 0:
                left -= 1
                if left == 1:
                    break
        round += 1
        
    print(round)
    for i in range(1, N+1):
        if len(cards[i]) == 0:
            continue
        print(i)
        print(" ".join([str(x) for x in cards[i]]))
        break           

while True:
    try:
        main()
    except EOFError:
        break