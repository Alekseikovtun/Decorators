from decorator_folder.decorator import loger_decorator as ld


@ld
def test_func(a, b):
    return a + b


if __name__ == '__main__':
    test_func(500, 500)
