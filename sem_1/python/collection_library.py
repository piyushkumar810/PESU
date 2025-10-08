# import collections
from collections import namedtuple

student=namedtuple("student",["name","age","course"])
s1=student("harry", 33, "potter")

print(s1.name)
print(s1.age)
print(s1.course)
print()

# --------------------- from collections importing dequq
from collections import deque

dq=deque(["a","b","c"])
dq.append("d")         # adding form right
dq.appendleft("z")     #  add to left
print(dq)

dq.pop()                #removing from right
dq.popleft()             # removing form left
print(dq)
print(type(dq))
print()

# -------------------------chainmap
from collections import ChainMap
default={"theme":"light", "language" : "English"}
user_setting={"theme" : "dark"}

config=ChainMap(user_setting,default)
print(config["theme"])
print(config["language"])
