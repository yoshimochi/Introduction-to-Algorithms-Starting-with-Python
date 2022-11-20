# 二分探索

def binary_search(data, value):
    left = 0 # 探索する範囲の左端を設定
    right = len(data) - 1 # 探索する範囲の右端を設定

    while left <= right:
        mid = (left + right) // 2 # 探索する範囲の中央を設定

        if data[mid] == value:
            # 中央の値を一致した場合は位置を返す
            return mid
        elif data[mid] < value:
            # 中央の値より大きい場合は探索の範囲を左に変更する
            left = mid + 1
        else:
            # 中央の値より小さい場合は探索の範囲を右に変更する
            right = mid - 1

    return -1


data: list = [50, 30, 90, 10, 20, 70, 60, 40, 80]
print(binary_search(sorted(data), 90))
