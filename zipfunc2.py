l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
# how to make pair or (1,5).(2,6)..... and how to make saprate list of 1,2,..... and 5,6.......
l = list(zip(l1, l2))
print(l)  # -- [(1, 5), (2, 6), (3, 7), (4, 8)]
# seprating
print(list(zip(*l)))  # --> [(1, 2, 3, 4), (5, 6, 7, 8)]
l3, l4 = list(zip(*l))
print(l3)  # --> (1, 2, 3, 4)
print(l4)  # --> (5, 6, 7, 8)
maxx = []
for pair in zip(l4, l3):
    maxx.append(max(pair))
print(maxx)  # --> [5, 6, 7, 8]
