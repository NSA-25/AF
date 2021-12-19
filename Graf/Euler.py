from collections import deque
def Hierholzer(file, file2):
    f = open(file, "r")
    g = open(file2, "w")
    n, m = [int(n) for n in f.readline().split()]
    L = [[] for _ in range(n + 1)]
    for i in range(m):
        n1, n2 = [int(n) for n in f.readline().split()]
        L[n1].append(n2)
        L[n2].append(n1)
    for i in range(1, n):
        if len(L[i]) % 2:
            g.write("-1")
            return None
    circuit = []
    drum = deque()
    drum.append(1)
    while drum:
        u = drum[-1]
        if L[u]:
            v = L[u].pop()
            drum.append(v)
            L[v].remove(u)
        else:
            circuit.append(drum.pop())
    g.write(" ".join(str(x) for x in circuit[:-1]))
Hierholzer("ciclueuler.in", "ciclueuler.out")
