# First try to graph it on a paper
import itertools


def min_cost_paht(routes):
    start = "Namangan"
    vertices = list(itertools.permutations
                    (['Namangan', 'Tashkent', 'Bukhara', 'Samarkand', 'Fergana', 'Andijan', 'Termiz', 'Nukus'])
                    )
    distance = []
    for v in vertices:
        path = 0
        if v[0] == start:
            for i in range(len(v)-1):
                for r in routes:
                    temp = r.split()
                    if v[i] in r and v[i+1] in r:
                        path += int(temp[-1])
        if path != 0:
            distance.append(path)

    print(min(distance))


if __name__ == '__main__':
    file = open('input10.txt', 'r')
    routes = [route.strip() for route in file]
    print(min_cost_paht(routes))
