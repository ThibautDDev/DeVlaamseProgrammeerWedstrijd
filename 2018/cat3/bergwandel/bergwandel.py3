def setGrid(grid, x, y, char):
    grid[x][y] = chr(char)
    return grid, char+1


for testgeval in range(1, 1+int(input())):
    char = 65

    lijn = input().split(" ")
    breedte = int(lijn[0])
    hoogte = int(lijn[1])

    grid = []
    grid2 = []
    for i in range(hoogte):
        lijn = input().split(" ")
        l = []
        l2 = []
        for j in range(breedte):
            l += [int(lijn[j])]
            l2 += ["."]
        grid += [l]
        grid2 += [l2]
    #print(grid)
    #print(grid2)

    el = min(grid[0])
    xc, yc = 0, 0
    for i in range(hoogte):
        lijn = grid[i]
        if el >= min(lijn):
            el = min(lijn)
            xc, yc = i, lijn.index(min(lijn))
    #print(xc, yc, el)
    grid2, char = setGrid(grid2, xc, yc, char)
    
    canClimb = True
    while canClimb:
        mog = [999999, 999999, 999999, 999999]
        # [NOORD-OOST-ZUID-WEST]
        if xc > 0 and grid[xc-1][yc] > el:
            mog[0] = grid[xc-1][yc]
        
        if yc < breedte-1 and grid[xc][yc+1] > el:
            mog[1] = grid[xc][yc+1]
        
        if xc < hoogte-1 and grid[xc+1][yc] > el: 
            mog[2] = grid[xc+1][yc]
        
        if yc > 0 and grid[xc][yc-1] > el:
            mog[3] = grid[xc][yc-1]
    
        elt = min(mog)
        #print(mog, elt, el)
        if elt == 999999:
            canClimb = False
        else:
            el = elt
            ind = mog.index(el)

            if ind == 0:
                xc -= 1
            elif ind == 1:
                yc += 1
            elif ind == 2:
                xc += 1
            else:
                yc -= 1
            
            grid2, char = setGrid(grid2, xc, yc, char)

    
    for i in range(hoogte):
        print(f"{testgeval} {''.join(grid2[i])}")
    #print(grid2)



"""
1
5 5
32 30 40 26 25
44 7 12 15 19
10 8 5 7 57
9 1 3 6 25
7 5 2 44 78

"""
    