def knapsack(hdrives, capacity):
    hdrives.sort(reverse=True)
    counter = cap = 0
    for hdrive in hdrives:
        if cap >= capacity:
            return counter
        counter += 1
        cap += hdrive


if __name__ == '__main__':
    file = open('input7.txt', 'r')
    hdrives = [int(hdrive.strip()) for hdrive in file]
    print(knapsack(hdrives, 28625))
