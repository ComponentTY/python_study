def sunny(a, b, *args, **kwargs):
    print(a, b, args)
    print(kwargs)


if __name__ == '__main__':
    sunny(1, 2, 3, 4, 5, 6, city=1)
