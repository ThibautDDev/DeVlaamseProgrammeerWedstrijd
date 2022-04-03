testgevallen = int(input())

def print_matrix(M):
    print()
    print(" " * 5, "|", end=" ")
    for kolom in range(len(M)):
        print(f"{kolom:5}", end=" ")
    print("")
    print("-----", end="-")
    for kolom in range(len(M)):
        print("-----", end="-")
    print("-----")
    for rij in range(len(M)):
        print(f"{rij:5d}", end=' | ')
        for kolom in range(len(M)):
            if (kolom < rij):
                print(" "*5, end=" ")
            else:
                print(f"{M[rij][kolom]:5}", end=" ")
        print("|")


for testgeval in range(1, 1+testgevallen):
    maxlengte = int(input())
    woorden = input().split(" ")

    


    over = [[0 for kolom in range(len(woorden))] for rij in range(len(woorden))]
    cumu = [[0 for kolom in range(len(woorden))] for rij in range(len(woorden))]
    pijl = [[0 for kolom in range(len(woorden))] for rij in range(len(woorden))]

    # eerste element maken
    over[0][0] = maxlengte - len(woorden[0])
    cumu[0][0] = (over[0][0])**2
    pijl[0][0] = "#"

    # eerste rij
    for AW in range(1, len(woorden)):
        if (over[0][AW - 1] >= len(woorden[AW]) + 1):
            over[0][AW] = over[0][AW - 1] - len(woorden[AW]) - 1
            cumu[0][AW] = (over[0][AW])**2
            pijl[0][AW] = "<-"
        else:
            over[0][AW] = -1
            cumu[0][AW] = -1
            pijl[0][AW] = "X"

    # laatste rij
    for AW in range(1, len(woorden)):
        AR = AW
        over[AR][AW] = maxlengte - len(woorden[AW])
        cumu[AR][AW] = (over[AR][AW])**2 + cumu[AR-1][AW-1]
        pijl[AR][AW] = "^-"

    

    # middenste
    for AW in range(1, len(woorden)):
        for AR in range(1, AW):
            # Optie 1: nieuwe lijn -> kan altijd
            if (over[AR - 1][AW - 1] != -1):
                over_1 = maxlengte - len(woorden[AW])
                cumu_1 = (over_1)**2 + cumu[AR-1][AW-1]
                pijl_1 = "^-"
            else:
                over_1 = -1
                cumu_1 = -1
                pijl_1 = "X"

            # Optie 2: bijsteken op vorige -> controlle nodig voor lengte
            if (over[AR][AW - 1] >= len(woorden[AW]) + 1):
                over_2 = over[AR][AW - 1] - len(woorden[AW]) - 1
                VK = AW - 1
                while (pijl[AR][VK] != "^-"):
                    VK -= 1
                cumu_2 = (over_2)**2 + cumu[AR-1][VK-1]
                pijl_2 = "<-"
            else:
                over_2 = -1
                cumu_2 = -1
                pijl_2 = "X"
            
            # Kleinste cumu nemen
            if (cumu_1 == -1 and cumu_2 == -1):
                over[AR][AW] = -1
                cumu[AR][AW] = -1
                pijl[AR][AW] = "X"
            elif (cumu_1 == -1 and cumu_2 != -1):
                over[AR][AW] = over_2
                cumu[AR][AW] = cumu_2
                pijl[AR][AW] = pijl_2
            elif (cumu_1 != -1 and cumu_2 == -1):
                over[AR][AW] = over_1
                cumu[AR][AW] = cumu_1
                pijl[AR][AW] = pijl_1
            elif (cumu_1 <= cumu_2):
                over[AR][AW] = over_1
                cumu[AR][AW] = cumu_1
                pijl[AR][AW] = pijl_1
            else:
                over[AR][AW] = over_2
                cumu[AR][AW] = cumu_2
                pijl[AR][AW] = pijl_2
        
    print(woorden)
    print_matrix(over)
    print_matrix(cumu)
    print_matrix(pijl)

    # beste nemen
    print(testgeval, min([cumu[i][len(woorden)-1] for i in range(0, len(woorden)) if (cumu[i][len(woorden)-1] != -1)]))


"""
1
6
Dit is de tekst

3
6
Dit is de tekst
7
Perfect
10
Deze editie is de beste ooit


"""