# Stage 4 will be transposing a matrix
import sys


def gather_mtx(num=None):
    # assigning like this reqs a iterable, using map to convert the original
    # iterable to contain ints
    text1 = "Enter size of matrix"
    text2 = "Enter matrix"
    if num == 1:
        text1 = "Enter size of first matrix"
        text2 = "Enter first matrix"
    elif num == 2:
        text1 = "Enter size of second matrix"
        text2 = "Enter second matrix"
    x, y = map(int, input(text1).split())
    print(text2)
    mtx = build_matrix(x, y)
    return mtx


def build_matrix(x, y, auto=0):
    # the auto default param is so I can tell it to create a matrix
    # full of 0s in the specified size
    mtx = list()
    i = 0
    if auto == 0:
        while i < x:
            row = list(map(float, input().split()))
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


def const_mult(mtx3, x):
    result = build_matrix(len(mtx3), len(mtx3[0]), 1)
    for i in range(len(mtx3)):
        # iterate through columns
        for j in range(len(mtx3[0])):
            result[i][j] = mtx3[i][j] * x
    return result


def mtx_mult(mtx3, mtx4):
    result = list()
    # check if the matrices can be multiplied
    if len(mtx3[0]) == len(mtx4):
        result = build_matrix(len(mtx3), len(mtx4[0]), 1)
        for z in range(len(mtx3)):
            for p in range(len(mtx4[0])):
                summ = 0
                for j in range(len(mtx3[0])):
                    summ += mtx3[z][j] * mtx4[j][p]
                result[z][p] = summ
    else:
        print("The operation cannot be performed.")
        return None
    return result


def p_result(result):
    print("The result is:")
    for p in result:
        print(" ".join(list(map(str, p))))
    return


def t_md(mtx):
    result = build_matrix(len(mtx), len(mtx[0]), 1)
    for i in range(len(mtx)):
        for j in range(len(mtx[0])):
            result[j][i] = mtx[i][j]
    return result


def t_sd(mtx):
    result = build_matrix(len(mtx), len(mtx[0]), 1)
    for i in range(len(mtx)):
        p = len(mtx) - i - 1
        for j in range(len(mtx[0])):
            z = len(mtx[0]) - j - 1
            result[j][i] = mtx[p][z]
    return result


def t_v(mtx):
    result = build_matrix(len(mtx), len(mtx[0]), 1)
    for i in range(len(mtx)):
        for j in range(len(mtx[0])):
            z = len(mtx[0]) - j - 1
            result[i][z] = mtx[i][j]
    return result


def t_h(mtx):
    result = build_matrix(len(mtx), len(mtx[0]), 1)
    for i in range(len(mtx)):
        p = len(mtx) - i - 1
        for j in range(len(mtx[0])):
            result[p][j] = mtx[i][j]
    return result


while True:
    res = None
    ans = input("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit
Your choice:""")
    if ans == "1":
        mtx1 = gather_mtx(1)
        mtx2 = gather_mtx(2)
        res = add_mtx(mtx1, mtx2)
        p_result(res)
    elif ans == "2":
        mtx1 = gather_mtx()
        mult = float(input())
        res = const_mult(mtx1, mult)
        p_result(res)
    elif ans == "3":
        mtx1 = gather_mtx(1)
        mtx2 = gather_mtx(2)
        res = mtx_mult(mtx1, mtx2)
        p_result(res)
    elif ans == "4":
        ans = input("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line
Your choice:""")
        mtx1 = gather_mtx()
        if ans == "1":
            res = t_md(mtx1)
        elif ans == "2":
            res = t_sd(mtx1)
        elif ans == "3":
            res = t_v(mtx1)
        elif ans == "4":
            res = t_h(mtx1)
        p_result(res)
    elif ans == "0":
        sys.exit(0)
    else:
        pass
