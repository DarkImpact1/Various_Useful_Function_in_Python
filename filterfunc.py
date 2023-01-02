# filter is used to filter your demand from any function
# it returs those elements of sequence for which fucntion is true
def even(a):
    return a % 2 == 0


number = [1, 2, 3, 4, 4, 4, 3, 2, 42332, 42, 42, 23,
          2, 32, 321323235, 436, 46, 45, 35, 34634, 5, 36435]
is_even = list(filter(even, number))
print(is_even)
