import sys
sys.setrecursionlimit(10 ** 6)
def CTC(file, file2):        # 60 infoarena: time limit exceeded
    import collections
    f = open(file, "r")
    g = open(file2, "w")
    n, m = [int(n) for n in f.readline().split()]
    d = [[] for _ in range(n + 1)]
    for i in range(m):
        n1, n2 = [int(n) for n in f.readline().split()]
        d[n1].append(n2)
    ids = (n+1)*[0]
    lowlink = (n+1)*[0]
    ctc = []
    stack = collections.deque()
    onstack = (n+1)*[False]
    nid = 0
    def DFS(n):
        nonlocal nid
        nid += 1
        ids[n] = nid
        lowlink[n] = nid
        stack.append(n)
        onstack[n] = True
        for i in d[n]:
            if ids[i] == 0:
                DFS(i)
                lowlink[n] = min(lowlink[n], lowlink[i])
            elif onstack[i]:
                lowlink[n] = min(lowlink[n], ids[i])
        if lowlink[n] == ids[n]:
            k = stack.pop()
            c = [k]
            onstack[k] = False
            while k != n:
                k = stack.pop()
                onstack[k] = False
                c.append(k)
            ctc.append(c)
    for i in range(1, n + 1):
        if ids[i] == 0:
            DFS(i)
    g.write(str(len(ctc)))
    for c in ctc:
        g.write('\n'+" ".join(str(n) for n in c))
    f.close()
    g.close()
CTC("ctc.in", "ctc.out")
