# Mathimatika 1: Omada Askhsewn 10: Askhsh 65, 66


def print_board(b):
    """
    Prints a 2D board.
    """
    len_column = len(b)
    len_line = len(b[0])
    
    max_len = 0 # finds longest element
    for i in range(len_column):
        for j in range(len_line):
            if len(str(b[i][j])) > max_len:
                max_len = len(str(b[i][j]))

    print(("+" + "-"*(2+max_len))*len_column + "+")
    for j in range(len_line):
        print("|", end=" ")
        for i in range(len_column):
            a = max_len
            c = str(b[i][j])
            print(" "*((a - len(c))//2 + (len(c) + a)%2) + c + ((a - len(c))//2)*" ", end=" | ")
        print("")
    print(("+" + "-"*(2+max_len))*len_column + "+")


def euler_method(f, x, y, Dx, n):
    """
    f: function of x and y such that y' = f(x, y)
    (x[0], y[0]): starting location for the iterations
    Dx: step size
    n: number of iterations"""
    x = [x]
    y = [y]
    for i in range(1, n+1):
        x.append(round(x[i-1] + Dx, 4))
        y.append(round(y[i-1] + Dx * f(x[i-1], y[i-1]), 4))
    return x, y


x1,y1 = euler_method(lambda x,y: y*(1-y), 0, 0.5, 0.5, 10)
x2,y2 = euler_method(lambda x,y: y*(1-y), 0, 0.5, -0.5, 10)
x_list = ['x'] + x2 + x1
y_list = ['y'] + y2 + y1
i_list = ['i'] + [i%11 for i in range(len(max(x_list, y_list, key=len))+1)]


print_board([x_list, y_list, i_list])
