'''
二分探索

リストを半分に分けて目的の値を探す
for文を回してリストから目的の値を探すよりも早くゴールに辿り着くことができるが
探索対象のリストがソートされていることが条件となる
'''

def binary_search(data, value):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2
        if data[mid] == value:
            return  mid
        elif data[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    return -1



data : list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(binary_search(data, 90))