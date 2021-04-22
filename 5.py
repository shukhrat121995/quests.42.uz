def distance_from_origin(commands):
    right = 0
    left = 0
    for command in commands:
        if command[0] == 'R':
            right += int(command[1:])
        else:
            left += int(command[1:])
    # I don't understand why answer is 50
    return right, left


if __name__ == '__main__':
    file = open('input5.txt', 'r')
    commands = [command.strip() for command in file]
    print(distance_from_origin(commands))
