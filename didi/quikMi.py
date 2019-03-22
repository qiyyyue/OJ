import numpy as np
np.set_printoptions(suppress=True)

def big_mul(a, b):

    count_a = 0
    count_b = 0

    index = len(a) - 1
    if a.__contains__('.'):
        while(a[index] != '.'):
            count_a += 1
            index -= 1
        a = a[:len(a) - count_a - 1] + a[len(a) - count_a:]

    index = len(b) - 1
    if b.__contains__('.'):
        while (b[index] != '.'):
            count_b += 1
            index -= 1
        b = b[:len(b) - count_b - 1] + b[len(b) - count_b:]


    len_a = len(a)
    len_b = len(b)

    c = [0 for i in range(len_a+len_b)]
    for i in range (1, len_a + 1):
        iindex = len_a - i
        for j in range (1, len_b + 1):
            jindex = len_b - j
            tmp_c = a[iindex]*b[jindex]
            c_index = i + j - 2
            while(tmp_c != 0):
                c[len(c)-c_index-1] += tmp_c%10
                if c[len(c)-c_index-1] >= 10:
                    c[len(c) - c_index - 1] %= 10
                    c[len(c) - c_index - 2] += 1
                # print(tmp_c%10)
                tmp_c //= 10
                c_index += 1

    z_index = 0
    while c[z_index] == 0:
        z_index += 1
    c = c[z_index:]

    cc = c[:len(c) - count_a - count_b] + ['.'] + c[len(c) - count_a - count_b:]
    return cc

def lf(num):
    res = []
    num = str(num)
    for i in range(len(num)):
        if num[i] != '.':
            res.append(int(num[i]))
        else:
            res.append(num[i])

    # print(res)
    return res



def quik(b, e):
    result = [1]
    b = lf(b)
    while e != 0:
        if (e & 1) == 1:
            result = big_mul(result, b)
        e >>= 1
        b = big_mul(b, b)
        # print(b)

    if result[0] == '.':
        result = [0] + result
    res = ''
    for c in result:
        res += str(c)
    return res



if __name__ == '__main__':
    raw_input = input()
    input = raw_input.split(' ')
    i = 0
    while(i < len(input)):
        b = (float)(input[i])
        e = (int)(input[i + 1])
        print(quik(b, e) , end=' ')
        i += 2
