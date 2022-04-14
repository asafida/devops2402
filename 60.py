def get_name():
    current_name = input("enter your name: ")
    my_file = open("names.txt", "a")
    my_file.write(f"{current_name}\n")
    my_file.close()

def show_names():
    my_file = open("name.txt")
    for name in my_file.readlines():
        print(f"hello {name}")


with open("name.txt") as my_file:
    for line in my_file.readlines():
        print(line)