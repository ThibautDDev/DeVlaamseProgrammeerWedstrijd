for testgeval in range(1, 1+int(input())):
    
    rangen = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "B", "V", "H"]
    kleuren = ["K", "R", "H", "S"]

    kaarten = input().split(" ")
    eindKleur, startIndex = kaarten[0][0], rangen.index(kaarten[0][1:])
    kaarten.pop(0)

    kaarten2 = []
    for kaart in kaarten:
        kaarten2 += [(kaart[0], kaart[1:])]
    #kleur - rang

    volgorde = []
    for kaart in kaarten2:
        score = 10*rangen.index(kaart[1]) + kleuren.index(kaart[0])
        volgorde += [score]
    #print("v", volgorde)

    lst = ""
    for i in range(3):
        if volgorde[i] == min(volgorde):
            lst += "2"
        elif volgorde[i] == max(volgorde):
            lst += "0"
        else:
            lst += "1"
    #print(lst)

    xtr = 0
    if lst == "012":
        xtr = 6
    elif lst == "021":
        xtr = 5
    elif lst == "102":
        xtr = 4
    elif lst == "120":
        xtr = 3
    elif lst == "201":
        xtr = 2
    else:
        xtr = 1
    
    ind = startIndex + xtr
    if ind >= 13:
        ind -= 13
    
    print(f"{testgeval} {eindKleur}{rangen[ind]}")
    #print()