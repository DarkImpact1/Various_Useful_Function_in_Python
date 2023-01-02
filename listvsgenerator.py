# list vs generator

# memory usage

import time
# l = [i**2 for i in range(1, 1000000)]

# to check the memory usage open task manager and while you execute this line check the memory allocation
# g = (i**2 for i in range(1, 1000000))


t1 = time.time()
l = [i**2 for i in range(1, 10000000)]
t2 = time.time()
print(t2-t1)
# it will take few seconds
t3 = time.time()
g = (i**2 for i in range(1, 10000000))
t4 = time.time()
print(t4-t3)
# it won't take that much time
