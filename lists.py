# does not work. cannot input anything but strings
def capitalize(word):
    return word.upper()


def main():
    print('input a list to map')
    list = input(': ')
    output = map(capitalize, list)
    for word in output:
        print(word)


main()
