import random


def a_husband_b(setA, setB, list_m_name, list_g_name):
    A = set()
    for i in setA:
        if i in list_m_name:
            A.add(i)
    B = set()
    for i in setB:
        if i in list_g_name:
            B.add(i)
    S = []
    i = min(len(A), len(B))
    while i > 0:
        p = random.choice(list(A))
        q = random.choice(list(B))
        if p != q:
            S.append([p, q])
            i = i - 1
            A.remove(p)
            B.remove(q)
    return S


def a_test_b(setA, setB, list_m_name):
    A = set()
    for i in setA:
        if i in list_m_name:
            A.add(i)
    B = set()
    for i in setB:
        if i in list_m_name:
            B.add(i)
    R = []
    i = min(len(A), len(B))
    while i > 0:
        p = random.choice(list(A))
        q = random.choice(list(B))
        if p != q:
            R.append([p, q])
            B.remove(q)
            i = i - 1
            if [q, p] in R:
                R.remove([q, p])
                i = i+1
                B.add(q)
    return R



