def factorial(a):
    if a==1:
        return a
    else:
        return factorial(a-1)*a
print(factorial(4))

def fact(n):
    l=list(range(1,n+1))
    return reduce(lambda x,y: x*y, l)

[fact(i) for i in l1]
