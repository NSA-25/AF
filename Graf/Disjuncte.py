def Disjuncte(file, file2):                                               #0 infoarena Memory limit exceeded
    f = open(file, "r")                                                   #Afisarea este corecta
    g = open(file2, "w")
    n, m = [int(n) for n in f.readline().split()]
    L = []
    for i in range(m):
      L.append([int(n) for n in f.readline().split()])
    h = (n+1)*[0]
    tata = (n+1)*[0]
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
    for i in L:
        c, u, v = i
        if c == 1:
            Reuniune(u, v)
        else:
            if Reprezentare(u) != Reprezentare(v):
                g.write("NU" + "\n")
            else:
                g.write("DA" + "\n")
Disjuncte("disjoint.in", "disjoint.out")
