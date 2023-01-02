# it's full form is keywordArgument  and store every thing in dictionary like args store everything in tuple
# **kwargs ( double star operator)

# kwargs as a parameter
def func(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} : {v}")
    print(type(kwargs))


func(first_name="Mohit", last_name="Dwivedi")

# most important thing to remember is that when you pass keyword argument then kwarg will store it as a dictionary
# def func(name,**kwargs): # if you write any other parameter before kwargs then you must pass argument for that because kwargs will take all the keyword and argument like in this I didn't pass any argument for name therefore it will show error

#     for k, v in kwargs.items():
#         print(f"{k} : {v}")
#     print(type(kwargs))


# func(first_name="Mohit", last_name="Dwivedi")


# dctionary unpacking
d = {'name': 'mohit', 'lname': 'dwivedi', 'age': 19}
# func(d) this is not the way to call this function
func(**d)  # this is the correct way to call the function


# sequence to pass
# suppose we have *args , **kwargs, normal parameter, default parameter then the sequence is
# PADK
# normal parameter, args, default parameter, kwargs


def abc(name, *args, last_name="unknown", **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
