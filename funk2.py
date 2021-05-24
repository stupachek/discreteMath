import copy


def product1(X, Y):
    Z = copy.deepcopy(X)
    for j in X:
        for i in Y:
            if j != i:
                Z.append(i)
    return Z


def product2(X, Y):
    Z = list()
    for j in X:
        for i in Y:
            if j == i:
                Z.append(j)
    return Z


def product3(X, Y):
    Z = copy.deepcopy(X)
    for j in X:
        for i in Y:
            if j == i:
                Z.remove(j)
    return Z


def product4(setA, setB, list_R):
    U = []
    for i in list(setA):
        for h in list(setB):
            U.append([i, h])
    for i in list_R:
        for j in U:
            if i == j:
                U.remove(i)

    return U


