def vulLandkaartIn(tst, kaart, geg):
    #print(geg)
    for i in range(len(kaart)):
        lijn = kaart[i]        
        l = ""
        for j in range(len(kaart[0])):
            el = lijn[j]
            aantal = str(len(geg[el]))
            l += aantal
            l += " "
        l = l[:-1]
        print(f"{tst} {l}")

def refreshGegevens(gegevens):
    for k in gegevens.keys():
        lst = gegevens[k]
        gegevens[k] = list(set(lst))
    return gegevens

for testgeval in range(1, 1 + int(input(""))):
    lijn = input().split(" ")

    breedte = int(lijn[0])
    hoogte = int(lijn[1])

    kaart = []
    for i in range(hoogte):
        kaart += [input()]
    #print(kaart)

    gegevens = {"A":[]}

    if hoogte == 1:
        try:
            for i in range(1, breedte-1):
                el = kaart[0][i]
                #print(el)

                if el not in gegevens.keys():
                    gegevens[el] = []
                
                if el != kaart[0][i+1]:
                    gegevens[el]  += [kaart[0][i+1]]
                
                if el != kaart[0][i-1]:
                    gegevens[el] += [kaart[0][i-1]]
        except:
            pass

    elif breedte == 1:
        try:
            for i in range(1, hoogte-1):
                el = kaart[i][0]
                #print(el)

                if el not in gegevens.keys():
                    gegevens[el] = []
                
                if el != kaart[i+1][0]:
                    gegevens[el]  += [kaart[i+1][0]]
                
                if el != kaart[i-1][0]:
                    gegevens[el] += [kaart[i-1][0]]
        except:
            pass
    
    else:
        for i in range(hoogte):
            for j in range(breedte):
                
                el = kaart[i][j]
                #print(i, j, el, gegevens)

                if el not in gegevens.keys():
                    gegevens[el] = []

                if i > 0 and el != kaart[i-1][j]:
                    #print("1")
                    gegevens[el] += [kaart[i-1][j]]
                
                if i < hoogte-1 and el != kaart[i+1][j]:
                    #print("2")
                    gegevens[el] += [kaart[i+1][j]]
                
                if j > 0 and el != kaart[i][j-1]:
                    #print("3")
                    gegevens[el] += [kaart[i][j-1]]

                if j < breedte-1 and el != kaart[i][j+1]:
                    #print("4")
                    gegevens[el] += [kaart[i][j+1]]
                
                gegevens = refreshGegevens(gegevens)
    
    for k in gegevens.keys():
        lst = gegevens[k]
        gegevens[k] = list(set(lst))
    #print(gegevens)

    vulLandkaartIn(testgeval, kaart, gegevens)
    #print()
