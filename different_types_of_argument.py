# Arguments

# default

'''def amitsaxena(a,b,c=10):

    d = a+ b+c

    d1 = a+b -c

    return (d, d1)

print(amitsaxena(5, 6))

'''


# required

'''def amitsaxena(a,b,c):

    d = a+ b+c

    d1 = a+b -c

    return (d, d1)
    


amitsaxena(5, 6,7)

'''

# keyword

'''def amitsaxena(a, b, c=12):
    d = a + b + c

    d1 = a + b - c

    return (d, d1)


print(amitsaxena(6, 7,c=0))

'''

# variable length

def amit(*args, **kwargs):

    for i in args:

        print(len(i))

        print(i)


amit([1, 2, 3, 4, 5, 6, 7, 8, 9],{1:4})



