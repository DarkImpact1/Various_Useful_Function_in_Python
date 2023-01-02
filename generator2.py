# creating generators and checking how it works

# for example
def func(num):
    for i in range(1, num+1):
        print(i, end=",")


func(10)  # output----1,2,3,4,5,6,7,8,9,10

# now going to create generator


def func(num):
    for i in range(1, num+1):
        yield i


print(func(10))  # it will print the address of genrators

# now we can use this func as a iterator and do whatever we want but only once because once you use it it will delete the previous memory
for i in func(10):
    print(i, end=" ")
# output-->1 2 3 4 5 6 7 8 9 10
print("\n")
numbers = func(10)
for i in numbers:
    print(i, end="/")
    # output-->1/2/3/4/5/6/7/8/9/10/

# and now to check wether it deletes the previous data or not now if run again the above for loop then it shouldn't print any number because we had used previous data and now it should be deleted
for i in numbers:
    print(i, end="/")
# it wouldn't give any output because data once used will be deleted

# and we can convert that generator to list, tuple etc...
