"""Best Practices for Using Functional Programming in Python

see: https://kite.com/blog/python/functional-programming/
"""
from functools import reduce, partial


def main():
    ##
    print((lambda a, b: a + b)(3, 4))

    ##

    def add(a, b): return a + b
    print(add(3, 4))

    ##

    A = ['Octavia Butler', 'Isaac Asimov', 'Neal Stephenson',
         'Margaret Atwood', 'Usula K Le Guin', 'Ray Bradbury']
    # Returns list ordered by length of author name
    sorted(A, key=len)
    # Returns list ordered alphabetically by last name.
    sorted(A, key=lambda name: name.split()[-1])
    def get_last_name(n): return n.split()[-1]
    print(sorted(A, key=get_last_name))

    ##

    V = [1, 2, 3, 4, 5, 6]
    # Multiply every item by two
    # [2, 4, 6, 8, 10, 12]
    print(list(map(lambda x: x * 2, V)))
    # Take the factorial by multiplying the value so far to the next item
    # 1 * 1 * 2 * 3 * 4 * 5 * 6
    print(reduce(lambda acc, x: acc * x, V, 1))

    def fac(n): return reduce(
        lambda acc, x: acc * x,
        [*range(1, n+1)],
        1
    )
    print(fac(6))

    ##

    def power(base, exp): return base ** exp
    cube = partial(power, exp=3)
    print(cube(5))


if __name__ == "__main__":
    main()
