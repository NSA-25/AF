def sortaret(file, file2): # infoarena 0 Memory limit exceeded
    f = open(file, "r")
    g = open(file2, "w")
    n, m = [int(n) for n in f.readline().split()]
    d = [[] for _ in range(n + 1)]
    for i in range(m):
        n1, n2 = [int(n) for n in f.readline().split()]
        d[n1].append(n2)
    v = (n + 1) * [False]
    r = []
    def DFS(n):
        v[n] = True
        for k in d[n]:
            if v[k] is False:
                DFS(k)
        r.append(n)
    for i in range(1, n + 1):
        if v[i] is False:
            DFS(i)
    g.write(" ".join(str(n) for n in r[::-1]))
    f.close()
    g.close()
sortaret("sortaret.in", "sortaret.out")