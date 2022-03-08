for testgeval in range(int(input(""))):
    info = input().split(" ")
    rekken = [int(i) for i in info[1:]]
    rekken.sort(reverse=True)
    #print(rekken)

    boeken = []
    aantalBoeken = int(input(""))
    for i in range(aantalBoeken):
        info = input().split(" ")
        num, titel = int(info[0]), " ".join(info[1:])
        boeken += [[titel, num]]
    boeken.sort()
    #print(boeken)

    i = 0
    while len(boeken) != 0 and i < len(rekken):
        if rekken[i] >= boeken[0][1]:
            rekken[i] -= boeken[0][1]
            boeken.pop(0)
        else:
            i += 1
    
    if aantalBoeken == 0:
        output = 0
    elif len(boeken) == 0:
        output = i + 1
    else:
        output = "ONMOGELIJK"

    print(testgeval+1, output)
    #print()
    #print("-"*30)
    #print()