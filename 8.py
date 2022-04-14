import fibo
from fibo import fib , fib2
from fibo import fib as moshe

fib(100)
a = fib2(100)
fibo.fib(100)
moshe(100)

a = fibo.fib2(100)
for number in a:
    print(f"number: {number}")