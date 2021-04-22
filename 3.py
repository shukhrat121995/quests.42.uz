import re


def find_valid_passwords(passwords):
    counter = 0
    for password in passwords:
        if len(password) >= 8:
            regex = ("^(?=.*[a-z])(?=." +
                     "*[A-Z])(?=.*\\d)" +
                     "(?=.*[@#$]).+$")
            pattern = re.compile(regex)
            if pattern.fullmatch(password) is not None:
                print(password)
                counter += 1
    return counter


if __name__ == '__main__':
    file = open('input3.txt', 'r')
    passwords = [password.strip() for password in file]
    print(find_valid_passwords(passwords))
