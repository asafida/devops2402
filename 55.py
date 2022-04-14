my_file = open("read_my_contents.txt")
a = my_file.readlines()
print(a)
for line in a:
    print(line, end="")
