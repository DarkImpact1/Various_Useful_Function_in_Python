
# how actually iterate over any iterable object
l = [1, 2, 3]  # iterable
# for i in l:
# print(i)
i = iter(l)
print(next(i))
print(next(i))
print(next(i))
# firstly it call iter function and convert that it into iterator and then it calls next function and pass first element to i and then so on and for loop knows how many times it had to call next function


# we can only call next function for iterators like generators, map etc... we can not call next function for iterable

# print(next(l)) list is not an iterator it's a iterable...

# --> you can run loop on iterable as well as iterable

for i in map(lambda a: a**2, l):
    print(i)


# Generator are iterators....
# generator is a sequence like list but it's a iterator not iterable...

# here's a reason why we should use generators


# suppose we create a list and run a loop on that list
a = [5, 6, 7, 8]
# first of all it will create a list and allocate memory to that list and then when the loop will be executing.... it will take time
# and in the case of generator
# it generate one item at a time and you can do whatever you want with that item and after this when it generates another item first item will be vanish and not consume your memory
# so it will consume less memory as well as consume less time

# when to use generators ---- if you want to use your data repeatedly or you want to use your data multiple times then you should use list but if you want to use your data only once then you should use generators

# we use yield keyword to create a generator --- yield i
