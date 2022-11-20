# 問題1：閏年を判定
def leapYear(n):
    if (n % 100 == 0) and (n % 400 > 0):
        print('うるう年ではありません')
    elif n % 4 == 0:
        print('うるう年です')
    else:
        print('うるう年ではありません')


print(leapYear(2000))


# 問題2：西暦を和暦に変換
gengo = ['明治', '大正', '昭和', '平成', '令和']

def japaneseImperialYear(n):
    if n < 1912:
        year = n - 1868 + 1
        return gengo[0] + str(year) + '年'
    elif n < 1926:
        year = n - 1912 + 1
        return gengo[1] + str(year) + '年'
    elif n < 1989:
        year = n - 1926 + 1
        return gengo[2] + str(year) + '年'
    elif n < 2019:
        year = n - 1989 + 1
        return gengo[3] + str(year) + '年'
    else:
        year = n - 2019 + 1
        return gengo[4] + str(year) + '年'

print(japaneseImperialYear(2000))