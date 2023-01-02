# objective
# def a functiontake any no of lists containing number
# [1,2,3],[4,5,6],,[7,8,9]
# return average
# (1+4+7)/3,(2+5+8)/3,(3+6+9)/3
# and try to make this using lambda


def average_finder(*args):
    avg = []
    for pair in zip(*args):  # unpacking tuple
        avg.append(sum(pair)/len(pair))
    return avg


print(average_finder([1, 2, 3], [4, 5, 6], [7, 8, 9]))

# using lambda
average = lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]
print(average([1, 2, 3], [4, 5, 6], [7, 8, 9]))
