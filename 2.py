def find_winner(names):
    return (sorted(names, key = lambda s: sum(map(ord, s)), reverse=True))[0]


if __name__ == '__main__':
    file = open('input2.txt', 'r')
    names = [name.strip() for name in file]
    print(find_winner(names))