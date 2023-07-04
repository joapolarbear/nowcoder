INFINIT = 1e6
DEBUG = False
def debug(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)

def main():
    pass

while True:
    try:
        main()
    except EOFError:
        break