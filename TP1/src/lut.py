def LutSubSamp(N):
    L = [[0, 255, 0, 255, 0, 255]]
    n = 1
    while n < N:
        # search for the largest subspace
        volume = 0
        ibest = 0
        for i in range(n):
            v = (L[i][1] - L[i][0]) * (L[i][3] - L[i][2]) * (L[i][5] - L[i][4])
            if v > volume:
                volume = v
                ibest = i

        # Subspace extraction from the list
        SBS = L[ibest]
        if (n > 1):
            if (ibest == 0):
                L = L[1:]
            elif (ibest == n - 1):
                L = L[:-1]
            else:
                L = L[:ibest] + L[ibest + 1:]
        else:
            L = []

        # Search for the longest side
        dim = 1
        if ((SBS[3] - SBS[2]) >= (SBS[1] - SBS[0])) and ((SBS[3] - SBS[2]) >= (SBS[5] - SBS[4])):
            dim = 2
        if ((SBS[5] - SBS[4]) >= (SBS[1] - SBS[0])) and ((SBS[5] - SBS[4]) >= (SBS[3] - SBS[2])):
            dim = 3

        # split in 2 and list update
        SBS1 = SBS.copy()
        SBS2 = SBS.copy()
        if dim == 1:
            SBS1[1] = int((SBS[0] + SBS[1]) / 2)
            SBS2[0] = SBS1[1]
        elif dim == 2:
            SBS1[3] = int((SBS[2] + SBS[3]) / 2)
            SBS2[2] = SBS1[3]
        else:
            SBS1[5] = int((SBS[4] + SBS[5]) / 2)
            SBS2[4] = SBS1[5]
        L.append(SBS1)
        L.append(SBS2)

        # counter update
        n += 1

    # LUT creation
    LUT = [[0, 0, 0] for i in range(N)]
    for i in range(N):
        LUT[i][0] = int((L[i][0] + L[i][1]) / 2)
        LUT[i][1] = int((L[i][2] + L[i][3]) / 2)
        LUT[i][2] = int((L[i][4] + L[i][5]) / 2)
    return LUT