'''
8クイーン問題
'''
N = 8

# 斜めのチェック
def check(x, col):
    # 配置済みの行を逆順に調べる
    for i, row in enumerate(reversed(col)):
        if (x + i + 1 == row) or (x - i - 1 == row): # 左上と左下にクイーンが存在するかチェック
            return False
    return True

def search(col):
    if len(col) == N: # 全て配置できれば出力
        print(col)
        return

    for i in range(N):
        if i not in col: # 同じ行は使わない
            if check(i, col):
                col.append(i)
                search(col) # 再帰的に探索
                col.pop()

search([])