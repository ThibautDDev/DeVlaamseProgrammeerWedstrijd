for testgeval in range(1, 1+int(input())):
    lijn = input().split(" ")
    aantalPersonen = int(lijn[0])
    aantalLocaties = int(lijn[1])
    aantalWapens = int(lijn[2])

    allePersonen = [str(i) for i in range(1, 1 + aantalPersonen)]
    alleLocaties = [chr(i + 65) for i in range(aantalLocaties)]
    alleWapens = [chr(i + 97) for i in range(aantalWapens)]
    
    print(f"Personen: {allePersonen}, Locaties: {alleLocaties}, Wapens: {alleWapens}\n")

    db_ok = {}
    db_nok = {}
    res = {}
    for i in range(1, 5):
        db_ok[i] = set()
        db_nok[i] = set()
        res[i] = {}
    print(db_ok)
    print(db_nok)
    print()

    aantalVragen = int(input())
    for i in range(aantalVragen):
        vraag = input().split(" ")
        vSpeler = int(vraag[0])
        aSpeler = vraag[2]

        verdachte = vraag[1][0]
        locatie = vraag[1][1]
        wapen = vraag[1][2]
        print(vraag)

        spelers = [1, 2, 3, 4]
        vSpelerIndex = vSpeler - 1
        uitgeslotenSpelers = []

        if aSpeler != "X":
            aSpeler = int(aSpeler)
            db_ok[aSpeler].add(verdachte)
            db_ok[aSpeler].add(locatie)
            db_ok[aSpeler].add(wapen)

            aSpelerIndex = spelers.index(aSpeler)
            if aSpelerIndex < vSpelerIndex:
                uitgeslotenSpelers += spelers[:aSpelerIndex]
                uitgeslotenSpelers += spelers[vSpelerIndex+1:]
            else:
                uitgeslotenSpelers += spelers[vSpelerIndex+1:aSpelerIndex]
        else:
            uitgeslotenSpelers = list(spelers)
            uitgeslotenSpelers.remove(vSpeler)
        print("uitgesloten spelers:", uitgeslotenSpelers)

        for sp in uitgeslotenSpelers:
            db_nok[sp].add(verdachte)
            db_nok[sp].add(locatie)
            db_nok[sp].add(wapen)
        print("ok", db_ok)
        print("nok", db_nok)
        print()
    

    remainingItems = []
    antw = []
    for i in range(1, 5):
        lst = []
        for x in db_ok[i]:
            if x not in db_nok[i]: lst += [x]
            if x not in db_nok[i]: remainingItems += [x]
        antw += [lst]
    print(antw)
    print(remainingItems)




    # solved = False
    # if(len(antw[0]) == 2 and len(antw[1]) == 2 and len(antw[2]) == 2 and len(antw[3]) == 2): solved = True

    # while (not solved):
    #     if(len(antw[0]) == 2 and len(antw[1]) == 2 and len(antw[2]) == 2 and len(antw[3]) == 2): solved = True
        

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
