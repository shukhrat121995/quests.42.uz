def read_message(letters):
    data = []
    hash_table = {}
    for letter in letters:
        data.extend([letter.split(' , ')])
    res = []
    for d in data:
        if len(d) > 1:
            hash_table[int(d[0])] = d[1]
            res.append(int(d[0]))
        else:
            hash_table[int(d[0][:len(d[0])-2])] = ' '
            res.append(int(d[0][:len(d[0])-2]))

    answer = ""
    res.sort()
    for e in res:
        answer += hash_table[e]
    return len(answer)


if __name__ == '__main__':
    file = open('input9.txt', 'r')
    letters = [letter.strip() for letter in file]
    print(read_message(letters))