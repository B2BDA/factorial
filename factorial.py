def factorial(a):
    if a==1:
        return a
    else:
        return factorial(a-1)*a
print(factorial(4))