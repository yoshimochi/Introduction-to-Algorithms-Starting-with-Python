n = 18

result: str = ''

while n > 0:
    result = str(n % 2) + result
    n //=2

print(result)