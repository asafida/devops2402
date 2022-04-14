isTrue = False
a = 2
b = 2.5
secondarry = [1,2,3]
strOne = "One"
strThree = "Three"
if a < b and strOne != strThree:
    print ("a is lower then b")
elif a == b:
    print ("a equals b")
else:
    print("a is not lower then b")

if len(secondarry) > 2:
    print ("scondarry has more than 2 element")

c = 5
d = 5
e = [1, 2, 3]
f = [1, 2, 3]

if c == d:
    print("c equals d")
if c is d:
    print("c is d")
if e == f:
    print("e equals f")
if e is f:
    print("e is f")
if type(c) is int:
    print("c is an integer")