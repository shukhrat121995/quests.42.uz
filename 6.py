def count_impressive_tweets(likes):
    res = 0
    for i in range(1, len(likes)):
        if likes[i] > likes[i - 1]:
            res += 1
            print(likes[i])
    return res


if __name__ == '__main__':
    file = open('input6.txt', 'r')
    likes = [int(like.strip()) for like in file]
    print(count_impressive_tweets(likes))
