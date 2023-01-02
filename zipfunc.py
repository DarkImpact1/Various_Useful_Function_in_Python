# Zip function
# it makes a tuple of the repective items of two different list it doesn't matter either len of both list are same or not it will make a zip til len of small list
userid = ["user1", "user2", "user3"]
username = ["mohit", "vaibhav", "ritik"]
lastname = ["dwivedi", "dwivedi", "tiwari"]
lname = ["dwivedi", "dwivedi"]
# so zip will give me an iterator which will be in the form of tuple and it will be like
# ("user1","mohit"),("user2","vaibhav"),("user3","ritik")
# and you can convert it into list/tuple .....etc
# and you can convert it into dictionary for better result iff tuple have only two items...
# syntax-- zip(firstlist, secondlist,nlist)

print(zip(userid, username))  # address of iterator
# [("user1","mohit"),("user2","vaibhav"),("user3","ritik")]
print(list(zip(userid, username)))
# {'user1': 'mohit', 'user2': 'vaibhav', 'user3': 'ritik'}
print(dict(zip(userid, username)))
# [("user1","mohit","dwivedi"),("user2","vaibhav","dwivedi"),("user3","ritik","tiwari")]
print(list(zip(userid, username, lastname)))
# print(dict(zip(userid,username,lastname)) --- error
print(list(zip(userid, username, lname)))
# [('user1', 'mohit', 'dwivedi'), ('user2', 'vaibhav', 'dwivedi')] only two users will be appear because lname have only two inputs


# -------------------------------------------------------------------------------------------------------------
