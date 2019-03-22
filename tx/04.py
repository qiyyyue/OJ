import sys


def cal():
    n_m = list(map(int, sys.stdin.readline().strip().split()))
    n = n_m[0]
    m = n_m[1]

    white = list(map(int, sys.stdin.readline().strip().split()))
    black = list(map(int, sys.stdin.readline().strip().split()))

    b = 0
    w = 0

    tmp_2 = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if black[0] <= i and black[1] <= j and black[2] >= i and black[3] >= j:
                b += 1
            elif white[0] <= i and white[1] <= j and white[2] >= i and white[3] >= j:
                w += 1
            elif abs(j - i)%2 == 0:
                w += 1
            else:
                b += 1
    print(w, b)

def cal_tmp():
    n_m = list(map(int, sys.stdin.readline().strip().split()))
    n = n_m[0]
    m = n_m[1]

    white = list(map(int, sys.stdin.readline().strip().split()))
    black = list(map(int, sys.stdin.readline().strip().split()))

    b = 0
    w = 0

    tmp_w = 0
    tmp_b = 0

    if (n*m)%2 == 0:
        tmp_w = (n*m)//2
        tmp_b = (n*m)//2
    else:
        tmp_w = (n * m) // 2 + 1
        tmp_b = (n * m) // 2

    StartX = min(black[0], white[0])  # 外包框在x轴上左边界
    EndX = max(black[2],
               )  # 外包框在x轴上右边界
    StartY = min(y11, y21)  # 外包框在y轴上上边界
    EndY = max(y12, y22)  # 外包框在y轴上下边界
    # 相交矩形区域的宽度和高度，因为这两个矩形的边都是平行与坐标轴的，因此他们的相交区域也是矩形
    # 那什么条件下才能形成相交区域啦，矩形是二维的，只有x,y方向都有交集时，他们才能形成相交区域
    # 记住上面提到过得外包框，就比较容易理解相交的条件了,blog1中的逆向思维也是不错的，不过感觉还是有些麻烦不直观，
    # 因此在这里多解释一下
    CurWidth = (black[2] - black[0]) + (x22 - white[0]) - (EndX - StartX)  # (EndX-StartX)表示外包框的宽度
    CurHeight = (y12 - y11) + (y22 - y21) - (EndY - StartY)  # (Endy-Starty)表示外包框的高度

    if CurWidth <= 0 or CurHeight <= 0:  # 不相交
        return []
    else:  # 相交
        X1 = max(black[0], white[0])  # 有相交则相交区域位置为：小中取大为左上角，大中取小为右下角
        Y1 = max(y11, y21)
        X2 = min(black[2], x22)
        Y2 = min(y12, y22)

    Area = CurWidth * CurHeight

n = int(sys.stdin.readline().strip())
for i in range(n):
    cal()
