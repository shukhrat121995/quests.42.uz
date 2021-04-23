# solution from https://www.geeksforgeeks.org/look-and-say-sequence/
def count_and_say(n):
    if n == 1:
        return "1"
    if n == 2:
        return "11"

    previous = "11"

    for i in range(3, n+1):
        previous += "$"
        l = len(previous)

        cnt = 1
        tmp = ""

        for j in range(1, l):
            # If current character
            # does't match
            if (previous[j] != previous[j - 1]):
                # Append count of
                # str[j-1] to temp
                tmp += str(cnt + 0)

                # Append str[j-1]
                tmp += previous[j - 1]

                # Reset count
                cnt = 1
            # If matches, then increment
            # count of matching characters
            else:
                cnt += 1
        previous = tmp

    return len(previous)


if __name__ == '__main__':
    print(count_and_say(42))
