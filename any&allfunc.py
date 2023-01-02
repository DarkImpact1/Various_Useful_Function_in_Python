n1 = [2, 4, 6, 8]
n2 = [1, 2, 3, 4, 5, 6, 7, 8]
# task = kya n2 or n2 me sare number even hai ?
n = [i % 2 == 0 for i in n1]
print(n)
print(all(n))  # agr sare value true honge to ye true return krega other wise false
# mtlb all hme true ya fr False boolean return krta hai ... and agr kisi list me sare value True hai to ye true return krega nhi to false....

n = [i % 2 == 0 for i in n2]
print(n)
print(all(n))
print(any(n))  # aur any hmein True tb dega agr koi bhi ek value true hogi tb
