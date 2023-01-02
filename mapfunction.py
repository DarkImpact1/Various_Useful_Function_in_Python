# map function is very useful function with the help of this we can use function as well as iterable object
# like
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def cube(a):
    return a**3
# so if we want another list in which we have cube of the list l, to achieve our goal we have several methods like with the use of args call the function and pass this list after unpacking by using *operator, using list comprehension also as well as there are several ways to achieve this target .... here's the question what make map function different from them is .... they make your program short and beautiful.

# and remember whatever the output you get using map function ... that output is iterable
# other one is with the help of map function we can use another function and iterable object and we can store the final output tuple, string, list whatever we want

# ex...

# map(nameoffunction, iterable object)


cubes = list(map(cube, l))
print(cubes)

# even sometimes we don't have to def function directly we can use lambda and use it in map function
square = list(map(lambda a: a**2, l))
print(square)


# now here i'm going to show you those different methods to print a list in which you'll have square of our list
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# begginers method
square = []
for i in number:
    square.append(i**2)
print(square)

# using *args

square = []


def sqre(*args):
    for i in args:
        square.append(i**2)
    return square


print(sqre(*number))


# using list comprehensiton:

sq = [i**2 for i in number]
print(sq)

# atlast
# using map
s = list(map(lambda a: a**2, number))
print(s)


# I hope you understand it
