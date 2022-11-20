# 線形探索を関数として定義し、値が見つかったら位置を返す
def linear_search(data, value):
    for i in range(len(data)):
        if data[i] == value:
            return i

    return -1


data: list = [50, 30, 90, 10, 20, 70, 60, 40, 80]
print(linear_search(data, 40))
