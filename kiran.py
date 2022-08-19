def add(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return ("it cannot perform")


x = add(10, 20)
print(x)


