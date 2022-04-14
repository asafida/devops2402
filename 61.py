try:
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))
    result = a / b
    print(result)

except ZeroDivisionError as e:
    print("could not divide by zero")
except ValueError as e:
    print("one of the variables is not a number")
except BaseException as e:
    print("something went wrong:" + str(e.args))
print("finished")

try:
    x = 1/0
except ZeroDivisionError as e:
    print("could not divide by zero")
finally:
    print("finally")

try :
 x = 1
finally:
 print("finally")
