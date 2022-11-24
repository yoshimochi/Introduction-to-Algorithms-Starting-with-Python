# ハノイの塔

def hanoi(n, src, dist, via):
    if n > 1:
        hanoi(n - 1, src, via, dist) # n-1枚を移動元から経由場所に移す
        print(src + ' ->' + dist)
        hanoi(n - 1, via, dist, src) # n-1枚を経由場所から移動先に移す
    else:
        print(src + ' ->' + dist)

n = int(input())
hanoi(n, 'a', 'b', 'c')