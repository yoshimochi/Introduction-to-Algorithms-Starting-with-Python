# 10進数　→　n進数へ変換

n = 18


def convert(n, base):
    result: str = ''

    while n > 0:
        result = str(n % base) + result
        n //= base

    return result


print(convert(n, 2))
print(convert(n, 3))
print(convert(n, 8))
