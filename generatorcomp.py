# like list comprehension we use generator comprehension what we have to do is we have to use paranthesis at the place of square brackets

square = [i**2 for i in range(1, 11)]
print(square)

# for generator

cube = (i**3 for i in range(1, 11))
print(cube)
# output-> address of generators

for i in cube:
    print(i, end=" ")
# cube of all num
for i in cube:
    print(i)
# output--> nothing because we had used generator once
