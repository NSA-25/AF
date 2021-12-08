from sys import setrecursionlimit
setrecursionlimit(10 ** 6)
def Darb(file, file2):
    f = open(file, "r")
    g = open(file2, "w")
    n = int(f.readline())
    L = [[] for _ in range(n + 1)]
    for i in f:
        u, v = [int(n) for n in i.split()]
        L[u].append(v)
        L[v].append(u)
    viz = (n+1)*[False]
    viz[1] = True
    r = 1
    u = 1
    def DFS(n, h):
        nonlocal r, u
        h += 1
        if h > r:
            r = h
            u = n
        viz[n] = True
        for k in L[n]:
            if viz[k] is False:
                DFS(k, h)
    def DFS2(n, h):
        nonlocal r
        h += 1
        if h > r:
            r = h
        viz[n] = False
        for k in L[n]:
            if viz[k]:
                DFS2(k, h)
    DFS(1, 0)
    r = 0
    DFS2(u, 0)
    g.write(str(r))
Darb("darb.in", "darb.out")