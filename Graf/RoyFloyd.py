def royfloyd(file, file2):
    f = open(file, "r")
    g = open(file2, "w")
    M = []
    n = int(f.readline())
    for i in range(n):
        l = [float('inf') if (e == 0) else e for e in [int(n) for n in f.readline().split()]]
        l[i] = 0
        M.append(l)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if M[i][j] > M[i][k] + M[k][j]:
                    M[i][j] = M[i][k] + M[k][j]
    g.write(('\n'.join([' '.join([str(i) for i in l]) for l in M])))
royfloyd("royfloyd.in", "royfloyd.out")