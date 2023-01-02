# ye for loop ke sath use hota hai and iski help se hm items ki position track krte hai
alpha = ['a', 'b', 'c', 'd']
pos = 0
for name in alpha:
    print(f"{pos}----{name}")
    pos += 1
# output---
# 0----a
# 1----b
# 2----c
# 3----d

# now printing same using enumerate

for pos, name in enumerate(alpha):
    print(f"{pos}----{name}")
# output
# 0----a
# 1----b
# 2----c
# 3----d
