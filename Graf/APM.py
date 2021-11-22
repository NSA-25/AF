def Kruskal(file, file2):                                                #90 infoarena Memory limit exceeded
    f = open(file, "r")
    g = open(file2, "w")
    n, m = [int(n) for n in f.readline().split()]
    L = []
    for i in range(m):
      L.append([int(n) for n in f.readline().split()])
    L.sort(key=lambda k: k[2])
    h = (n+1)*[0]
    tata = (n+1)*[0]
    R = []
    cost = 0
    def Reprezentare(u):
        while tata[u] != 0:
            u = tata[u]
        return u
    def Reuniune(u, v):
        ru, rv = Reprezentare(u), Reprezentare(v)
        if h[ru] > h[rv]:
            tata[rv] = ru
        else:
            tata[ru] = rv
            if h[ru] == h[rv]:
                h[rv] += 1
    i = 0
    while len(R) < n - 1:
        if Reprezentare(L[i][0]) != Reprezentare(L[i][1]):
            u, v, c = L[i]
            R.append((u, v))
            cost += c
            Reuniune(u, v)
        i += 1
    g.write(str(cost) + "\n" + str(n-1))
    for m in R:
        g.write("\n" + " ".join(str(n) for n in m))
Kruskal("apm.in", "apm.out")
