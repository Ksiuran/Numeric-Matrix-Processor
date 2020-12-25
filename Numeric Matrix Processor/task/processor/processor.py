# Start with matrix addition
import sys


def build_matrix(x, y, auto=0):
    mtx = list()
    i = 0
    if auto == 0:
        while i < x:
            row = list(map(int, input().split()))
            if len(row) == y:
                mtx.append(row)
                i += 1
    else:
        while i < x:
            mtx.append([0] * y)
            i += 1
    return mtx


def add_mtx(mtx3, mtx4):
    if len(mtx3) == len(mtx4) and len(mtx3[0]) == len(mtx4[0]):
        result = build_matrix(len(mtx3), len(mtx3[0]), 1)
        # iterate through rows
        for i in range(len(mtx3)):
            # iterate through columns
            for j in range(len(mtx3[0])):
                result[i][j] = mtx3[i][j] + mtx4[i][j]
        return result
    else:
        print("ERROR")
        sys.exit(0)


# assigning like this reqs a iterable, using map to convert the original
# iterable to contain ints
x1, y1 = map(int, input().split())
mtx1 = build_matrix(x1, y1)
x2, y2 = map(int, input().split())
mtx2 = build_matrix(x2, y2)
res = add_mtx(mtx1, mtx2)
for i in res:
    print(" ".join(list(map(str, i))))