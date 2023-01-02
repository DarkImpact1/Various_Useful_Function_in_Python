# abhi tak hm max or min function ka basic use padhte aaye hai jaise kisi list me se maximim number and minimum number kaise find krenge

# num = [1, 2, 3, 4, 4, 5, 67, 7, 8, 8, 12]
# print(max(num))#------ 67
# print(min(num))#------1


# ab hm ye dekhenge ki kaise hm max aur min advance level me kaise use kr skte hai
name = ['mohit', 'vaibhav', 'kuldeep', 'manoharlal']
# print(max(name))----- wouldn't return expected output
# so ab hmein max ko explain krna hoga ki hme kis cheej ke according max chaiye

# max(kis cheej me se, key= ek functin jiske according hm max find krna chahte hai)

# print(max(name, key=len(name)) -----yahan hm len use nhi kr skte kuki len hmein ek int output dega and key ko ek function chaiye na ki integer


def func(item):
    return len(item)


print(max(name, key=func))  # -- monoharlal
print(min(name, key=func))  # -- mohit

# ab jaise ki jo function hmne define kiya hai uska hm kahin use nhi kr rhe to hm uski place pr lambda use krenge


print(max(name, key=lambda item: len(item)))  # -- monoharlal

student = [
    {'name': 'mohit', 'score': 34, 'age': 20},
    {'name': 'kuldeep', 'score': 35, 'age': 20},
    {'name': 'vaibhav', 'score': 36, 'age': 20}
]
# jaise ki ab ham chahte hai ki is dictionary se vo name print kre jisne sbse jyada score kiya hai  to hm max function ka use kr skte hai
print(max(student, key=lambda item: item.get('score')))
#output-{'name': 'vaibhav', 'score': 36, 'age': 20}
# and isme se iska name print krwane ke liye

print(max(student, key=lambda item: item.get('score'))['name'])
# -----------------------------------------------------------------------------------------------------------
students = {
    'mohit': {'score': 500, 'age': 23},
    'harshit': {'score': 40, 'age': 22},
    'vaibhav': {'score': 60, 'age': 24}
}
# jaise ki ab ham chahte hai ki is dictionary se vo name print kre jisne sbse jyada score kiya hai  to hm max function ka use kr skte hai


print(max(students, key=lambda item: students[item]['score']))
