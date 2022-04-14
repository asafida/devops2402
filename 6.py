my_range = list(range(5))
print(my_range)
my_range1 = list(range(-2, 5))
#From-To
print(my_range1)
my_range2 = list(range(-2, 5, 3))
#טווח מספרים בקפיצה של 3
print(my_range2)

for i in range(-9, 5 ,2):
    print(i)
names = ["asaf", "ida", "cohen"]
for name in names:
    if name  == "asaf":
        continue
    print(name)
    if name == "ida":
     print("ida is in the bilding!")
    break
#break stop runs function.
#contiue מדלג על ההדפסה

for i in range(len(names)):
    print(names[i])

#לולאה חוזרת
a = 0
while a < 5:
    print(a)
    a = a + 1
else:
    print("Done")


if  a == 0:
    pass
else:
    print (" a is not o")