
# should be edited, cause there's 2TB space left
def knapsack(weights, capacity):
    weights.sort(reverse=True)
    counter = 0
    for weight in weights:
        if capacity > weight:
            counter += 1
            capacity -= weight

    return counter, capacity


if __name__ == '__main__':
    file = open('input7.txt', 'r')
    hdrives = [int(hdrive.strip()) for hdrive in file]
    print(knapsack(hdrives, 28625))
