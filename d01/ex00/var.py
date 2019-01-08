def my_var():
    a = 42
    b = "42"
    c = "quarante-deux"
    d = 42.0
    e = True
    f = [42, 42.0]
    g = {42: 42}
    h = (42,)
    i = set()
    for var in [a, b ,c ,d, e, f, g, h, i]:
        print("{0} est de type {1}".format(var, type(var)))

if __name__ == '__main__':
    my_var()