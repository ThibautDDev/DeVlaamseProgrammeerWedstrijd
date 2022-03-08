for testgeval in range(1, 1+int(input(""))):
    aantalStations = int(input(""))
    
    dictStations = dict()
    for i in range(aantalStations):
        lst = list(map(int, input("").split(" ")))
        dictStations[i] = lst
    #print("print:", dictStations)

    aantalPersonen = int(input(""))
    vertrek = list(map(int, input("").split(" ")))
    aankomst = list(map(int, input("").split(" ")))

    dictPersonen = dict()
    for i in range(aantalPersonen):
        kost = dictStations[vertrek[i] - 1][aankomst[i] - 1]
        lst = [(vertrek[i]-1, aankomst[i]-1), aankomst[i]-1, kost]
        dictPersonen[i] = lst
    #print("print:", dictPersonen)
    
    totaleWinst = 0
    i = 0
    while (i < aantalPersonen):
        j=i+1
        while (j < aantalPersonen):
            persooni = dictPersonen[i]
            persoonj = dictPersonen[j]
            if (persooni[2] > 0 and persoonj[2] > 0 and persooni[1] == persoonj[0][0] and persoonj[1] == persooni[0][0]):
                kosti = persooni[2]
                kostj = persoonj[2]
                
                persooni[2] = kosti - kostj
                persoonj[2] = kostj - kosti
                totaleWinst = kosti + kostj
                dictPersonen[i] = persooni
                dictPersonen[j] = persoonj
            #else:
                #print("geen verbetering mogelijk")
            #print(i, j)
            j+=1
        i+=1



    print()
    print(f"{testgeval} {totaleWinst}")
    print()

"""
1
5
0 1 2 3 4
1 0 2 3 4
2 2 0 4 1
3 3 4 0 1
4 4 1 1 0
3
1 2 5
5 3 1

"""