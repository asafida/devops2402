
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
