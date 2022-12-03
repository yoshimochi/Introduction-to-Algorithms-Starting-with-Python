# シンプルな線形探索
data: list = [50, 30, 90, 10, 20, 70, 60, 40, 80]
found: bool = False

for i in range(len(data)):
    if data[i] == 40:
        print(i)
        found = True
        break

if not found:
    print('Not Found')