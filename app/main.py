BASE36_CHARS = "0123456789abcdefghijklmnopqrstuvwxyz"


def encode(num):
    return len(BASE36_CHARS)


def main():
    print(encode(0))


main()
