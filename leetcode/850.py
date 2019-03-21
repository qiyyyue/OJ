# coding: usf-8
'''
计算矩形面积
'''



def rectangleArea(rectangles):
    """
    :type rectangles: List[List[int]]
    :rtype: int
    """

    y_list = []

    for i in range(len(rectangles)):
        y_list.append(rectangles[i][1])
        y_list.append(rectangles[i][3])

    y_set = set(y_list)
    y_set = sorted(y_set)

    sum_area = 0

    for i in range(len(y_set) - 1):
        y_l = y_set[i]
        y_h = y_set[i + 1]

        sum_area += cal_one_y_area(y_l, y_h, rectangles)
    return sum_area

def cal_one_y_area(y_l, y_h, rectangles):

    tmp_x_len = 0

    x_list = []
    for i in range(len(rectangles)):
        if rectangles[i][1] <= y_l and rectangles[i][3] >= y_h:
            x_list.append(rectangles[i][0])
            x_list.append(rectangles[i][2])

    x_set = set(x_list)
    x_set = sorted(x_set)

    for i in range(len(x_set) - 1):
        x_l = x_set[i]
        x_h = x_set[i + 1]
        for j in range(len(x_list )//2):
            x_1 = x_list[j*2]
            x_2 = x_list[j*2 + 1]
            if x_1 <= x_l and x_2 >= x_h:
                tmp_x_len += (x_h - x_l)
                break
    return tmp_x_len *(y_h - y_l)

rectangles = [[0,0,1000000000,1000000000]]

res = rectangleArea(rectangles)
print(res)
print(res%(1000000007))