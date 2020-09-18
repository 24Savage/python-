import sys

while True:
    try:
        n, a = [int(i) for i in sys.stdin.readline().strip().split()]
        b = [int(i) for i in sys.stdin.readline().strip().split()]
        for i in range(n):
            if b[i] <= a:
                a += b[i]
            else:
                x, y = b[i], a
                mod = x%y
                while mod :
                    x, y = y, mod
                    mod = x%y
                a += y
        print(a)
    except:
        break