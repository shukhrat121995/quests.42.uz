# First try to graph it on a paper, and you will see that after visiting each vertices you have to pick the smallest
# one which is not in your visited list
import sys


def min_cost_paht(routes):
    start = 'Namangan'
    visited = list()
    visited.append(start)
    res = 0

    while len(visited) < 8:
        minimum = sys.maxsize
        name = ""
        for route in routes:
            if start in route:
                temp = route.split()
                if int(temp[4]) < minimum and (temp[0] not in visited or temp[2] not in visited):
                    minimum = int(temp[4])
                    if temp[0] != start:
                        name = temp[0]
                    else:
                        name = temp[2]
        start = name
        print(minimum)
        res += minimum
        visited.append(start)

    return visited, res


if __name__ == '__main__':
    file = open('input10.txt', 'r')
    routes = [route.strip() for route in file]
    print(min_cost_paht(routes))
