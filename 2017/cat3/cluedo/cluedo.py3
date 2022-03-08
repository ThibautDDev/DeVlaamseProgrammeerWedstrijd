for testgeval in range(1, 1+int(input())):
    lijn = input().split(" ")

    personen = [i for i in range(1, 1+int(lijn[0]))]
    locatie = [chr(i + 65) for i in range(int(lijn[1]))]
    wapen = [chr(i + 97) for i in range(int(lijn[2]))]
    print(personen, locatie, wapen)

    gegevens = {}
    for i in range(1, 5):
        gegevens[i] = [list(personen), list(locatie), list(wapen)]
    print(gegevens)
    print()

    spelers = [1, 2, 3, 4]
    aantalVragen = int(input(""))
    zetten = []
    for i in range(aantalVragen):
        lijn = input("")
        zetten += [lijn]
        lijn = lijn.split(" ")
        s = int(lijn[0])
        sp = int(lijn[1][0])
        l = lijn[1][1]
        w = lijn[1][2]
        a = lijn[2]
        
        spelerIndex = spelers.index(s)
        uitgeslotenSpelers = []
        if a != "X":
            a = int(a)
            antSpelerIndex = spelers.index(a)
            if antSpelerIndex < spelerIndex:
                uitgeslotenSpelers += spelers[:antSpelerIndex]
                uitgeslotenSpelers += spelers[spelerIndex+1:]
            else:
                uitgeslotenSpelers += spelers[spelerIndex+1:antSpelerIndex]
        else:
            uitgeslotenSpelers = list(spelers)
            uitgeslotenSpelers.remove(s)
        
        #print("uitgesloten spelers:", uitgeslotenSpelers)
        print()

        for speler in uitgeslotenSpelers:
            #print(speler, gegevens[speler])
            if sp in gegevens[speler][0]:
                gegevens[speler][0].remove(sp)
            if l in gegevens[speler][1]:
                gegevens[speler][1].remove(l)
            if w in gegevens[speler][2]:
                gegevens[speler][2].remove(w)

    print()
    print(30*'-')
    for k, v in gegevens.items():
        print(k, v)
        print()




"""
1
4 4 3
16
1 1Aa 2
2 2Db 4
3 4Ab 2
4 4Ac 2
1 1Cb X
2 4Cb 3
3 3Cc 4
4 2Bb X
1 2Da 2
2 3Ac 3
3 2Aa 2
4 3Cb 1
1 3Dc 3
2 4Ba 3
3 1Aa 1
4 2Dc X
"""
