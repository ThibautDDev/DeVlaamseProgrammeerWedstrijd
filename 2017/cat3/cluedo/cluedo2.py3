for testgeval in range(1, 1+int(input())):
    lijn = input().split(" ")
    aantalPersonen = int(lijn[0])
    aantalLocaties = int(lijn[1])
    aantalWapens = int(lijn[2])

    allePersonen = [i for i in range(1, 1 + aantalPersonen)]
    alleLocaties = [chr(i + 65) for i in range(aantalLocaties)]
    alleWapens = [chr(i + 97) for i in range(aantalWapens)]
    
    print(f"Personen: {allePersonen}, Locaties: {alleLocaties}, Wapens: {alleWapens}\n")

    db = {}
    uitkomst = {}
    for i in range(1, 5):
        db[i] = [list(allePersonen), list(alleLocaties), list(alleWapens)]
        uitkomst[i] = []
    print(db)
    print(uitkomst)
    print()


    aantalVragen = int(input())
    for i in range(aantalVragen):
        vraag = input().split(" ")
        vSpeler = int(vraag[0])
        aSpeler = vraag[2]
        
        verdachte = int(vraag[1][0])
        locatie = vraag[1][1]
        wapen = vraag[1][2]
        print(vraag)


        spelers = [1, 2, 3, 4]
        vSpelerIndex = vSpeler - 1
        uitgeslotenSpelers = []

        if aSpeler != "X":
            aSpeler = int(aSpeler)
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
            print(sp, db[sp])
            if verdachte in db[sp][0]:
                db[sp][0].remove(verdachte)
            if locatie in db[sp][1]:
                db[sp][1].remove(locatie)
            if wapen in db[sp][2]:
                db[sp][2].remove(wapen)
            print(sp, db[sp])
        print()
  

    r = {}
    itemsLeft = []
    for i in range(1, 5):
        print(db[i])
        items = sum(db[i], [])
        if len(items) == 2:
            r[i] = "".join(items)
            itemsLeft = [value for value in itemsLeft if value != r[i][0] and value != r[i][1]]
        itemsLeft += sum(db[i], [])   
    print(itemsLeft)




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
