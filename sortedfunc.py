alp = ['a', 'z', 'e', 's', 'q']
alp.sort()
print(alp)
# ['a', 'e', 'q', 's', 'z']
# ----------------------------------------------------------------------------------------
alp2 = ('a', 'z', 'e', 's', 'q')
# alp2.sort()---- won't run because tuple don't have any sort attribute
print(sorted(alp2))
print(alp2)
# ('a', 'z', 'e', 's', 'q') because tuple is immutable

# ['a', 'e', 'q', 's', 'z']
# --------------------------------------------------------------------------
alp3 = {'a', 'z', 'e', 's', 'q'}
print(sorted(alp3))
# ['a', 'e', 'q', 's', 'z']
print(alp3)
# {'z', 'a', 'e', 'q', 's'}


# -------------------- ADVANCE SORTING---------------------------------------
# working on complex data structure
guitars = [
    {'model': 'yamaha f310', 'price': 94000},
    {'model': 'faith f310', 'price': 90000},
    {'model': 'taylor f310', 'price': 50000}
]
print(sorted(guitars, key=lambda item: item['price']))
#-- [{'model': 'taylor f310', 'price': 50000}, {'model': 'faith f310', 'price': 90000}, {'model': 'yamaha f310', 'price': 94000}]

print(sorted(guitars, key=lambda item: item['price'], reverse=True))
#-- [{'model': 'yamaha f310', 'price': 94000}, {'model': 'faith f310', 'price': 90000}, {'model': 'taylor f310', 'price': 50000}]
