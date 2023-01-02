# * operator or * args
def total(a, b):
    return a+b
# * args take multiple input and convert it into tuple


print(total(1, 2))
# but it won't take more than two input hence to overcome that we use *operator


def all_total(*args):  # here we can write anything at the place of args we use to write it as args because it is the apropriate
    total = 0
    for i in args:
        total += i
    return total


print(all_total(1, 2, 3, 4, 4, 5, 6, 6, 7))


# ------------------------------------------------------------------------------------------------------------- and if we pass any normal parameter  then that will be excluded at it won't be the part of the this function
# unpacking.
# we can't pass a list, tuple in function so in order to pass list or tuple or group of multiple number first we unpack them using *operator and then pass it into function

l = [1, 2, 3, 4, 4, 5, 6, 6, 7, 78, 8]
# print(all_total(l)) will show error
print(all_total(*l))

# sequence to pass
# suppose we have *args , **kwargs, normal parameter, default parameter then the sequence is
# PADK
# normal parameter, args, default parameter, kwargs


def abc(name, *args, last_name="unknown", **kwargs): #-> None
    print(name)
    print(args)
    print(last_name)
    print(kwargs)


abc("mohit", 1, 2, 3, 4, 5, a=2)
