def Hakimi(file, file2):
    f = open(file, "r")
    g = open(file2, "w")
    L = [int(n) for l in f.readlines() for n in l.split()]
    def Recursie(L):
        L.sort(reverse=True)
        n = L[0]
        L = L[1:]
        if n > len(L):
            return "Nu"
        if n == 0:
            return "Da"
        for i in range(n):
            L[i] -= 1
            if L[i] < 0:
                return "Nu"
        return Recursie(L)
    if sum(L) % 2 != 0:
        g.write("Nu")
    else:
        g.write(Recursie(L))
    f.close()
    g.close()
Hakimi("hakimi.in", "hakimi.out")
