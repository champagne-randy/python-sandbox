import json
import sys


s = "If Comrade Napoleon says it, it must be right."
a = [100, 200, 300]


def foo(arg):
    print(f'arg = {arg}')


class Foo:
    pass


def main():
    print(json.dumps(sys.path, indent=2))


if __name__ == "__main__":
    main()
