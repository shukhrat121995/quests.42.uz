def decode_message(message):
    alphabet = {
        '1': '',
        '2': 'a',
        '22': 'b',
        '222': 'c',
        '3': 'd',
        '33': 'e',
        '333': 'f',
        '4': 'g',
        '44': 'h',
        '444': 'i',
        '5': 'j',
        '55': 'k',
        '555': 'l',
        '6': 'm',
        '66': 'n',
        '666': 'o',
        '7': 'p',
        '77': 'q',
        '777': 'r',
        '7777': 's',
        '8': 't',
        '88': 'u',
        '888': 'v',
        '9': 'w',
        '99': 'x',
        '999': 'y',
        '9999': 'z',
        '0': ' ',
    }
    res = []

    temp = message[0]
    store = temp
    for i in range(1, len(message)):
        if temp != message[i]:
            temp = message[i]
            res.append(store)
            store = temp
        else:
            store += message[i]
        if i == len(message) - 1:
            res.append(store)
    result = ""
    for code in res:
        result += alphabet[code]
    return result


if __name__ == '__main__':
    print(decode_message("444333099966688027773303666444664044480229990442663099966688027773305887777809277778444664099966688777084446330844144477770827777550927777033277779990866602226661668444668833089997330663399808666084433083399802266699046661666305558822255"))
