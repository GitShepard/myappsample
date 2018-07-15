import os


def wrapper(oldfunc):
    def inside():
        print('hello')
        oldfunc()
        print('function finished')

    return inside

@wrapper
def s_printer():
    print('hello world')


if __name__ == "__main__":
    s_printer()
