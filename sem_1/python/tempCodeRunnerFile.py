def fibonacci():
    a = 0
    b = 1
    print(a)
    print(b)

    while True:
        c = a + b
        if c > 50:
            break
        print(c)
        a = b
        b = c

fibonacci()