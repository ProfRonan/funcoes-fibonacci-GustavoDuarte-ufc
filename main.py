def fibonacci(n):
    if n < 0:
        raise ValueError("n tem que ser maior do que zero")
    elif n == 0:
        b = 0
        return(b)
    elif n == 1 or n == 2:
        b = 1
        return(b)
    else:
        b = 1
        c = 0
        d = 0
        e = 0
        while c < n-2:
            d = b
            b = b + d - e
            e = b - d
            c += 1
        return(b)
