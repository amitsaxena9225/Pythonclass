global fac


def fact(n):

    fac = 1

    for i in range(1, n+1):

        fac = fac * (i)

    print(fac)


fact(5)
