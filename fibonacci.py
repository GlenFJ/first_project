def fib(num):
    a=0
    b=1
    for x in range(num):
        yield a
        temp=a
        a=b
        b=b+temp


for i in fib(5):
    print(i)