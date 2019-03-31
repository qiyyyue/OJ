from typing import List


def powerfulIntegers(x: int, y: int, bound: int) -> List[int]:
    res = set()
    i = 1
    j = 1
    while i <= bound:
        j = 1
        while i + j <= bound:
            print(i, j)
            res.add(i + j)
            j *= y
            if j == 1:
                break
        i *= x
        if i == 1:
            break
    return res


print(powerfulIntegers(3, 5, 15))
