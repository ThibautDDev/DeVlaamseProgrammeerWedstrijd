aantal_testgevallen = int(input())

def oosten(teken, kaart, diepte):
    aantal_rijen_, aantal_kolomen_ = aantal_rijen, aantal_kolomen
    start_rij_, start_kolom_ = start_rij, start_kolom
    x_, y_, z_ = x, y, z
    #print(aantal_rijen_, aantal_kolomen_)
    #print(start_rij_, start_kolom_)
    #print(x_, y_, z_)

    if (aantal_kolomen_ <= x_ - start_kolom_): # kaart te klein (kolomen)
        #print('Kolom toevoegen')
        aantal_kolomen_ += 1 # kolom toevoegen
        for rij in range(aantal_rijen_): # elke rij verlengen
            kaart[rij].append(default_teken)
            diepte[rij].append(default_diepte)
        #print(kaart)
        
    if (aantal_rijen_ <= y_ - start_rij_): # kaart te klein (rijen)
        #print('Rij toevoegen')
        aantal_rijen_ += 1 # rij toevoegen
        kaart.append([default_teken for i in range(aantal_kolomen_)])
        diepte.append([default_diepte for i in range(aantal_kolomen_)])
        #print(kaart)

    if (start_rij_ > y_): # kaart te klein (omhoog)
        #print('Rij toevoegen - omhoog')
        start_rij_ -= 1
        aantal_rijen_ += 1
        kaart = [[default_teken for i in range(aantal_kolomen_)]] + kaart
        diepte = [[default_diepte for i in range(aantal_kolomen_)]] + diepte
        #print(kaart)

    #print(f'gebruikte: {y_ - start_rij_}, {x_ - start_kolom_} ')

    if (diepte[y_ - start_rij_][x_ - start_kolom_] <= z_): # enkel als voor vorige is
        kaart[y_ - start_rij_][x_ - start_kolom_] = teken
        diepte[y_ - start_rij_][x_ - start_kolom_] = z_

    x_ += 1 # verplaats voor volgende

    return kaart, diepte, x_, y_, z_, aantal_rijen_, aantal_kolomen_, start_rij_, start_kolom_

def zuiden(teken, kaart, diepte):
    aantal_rijen_, aantal_kolomen_ = aantal_rijen, aantal_kolomen
    start_rij_, start_kolom_ = start_rij, start_kolom
    x_, y_, z_ = x, y, z
    #print(aantal_rijen_, aantal_kolomen_)
    #print(start_rij_, start_kolom_)
    #print(x_, y_, z_)
        
    if (aantal_rijen_ <= y_ - start_rij_): # kaart te klein (rijen)
        aantal_rijen_ += 1 # rij toevoegen
        kaart.append([default_teken for i in range(aantal_kolomen_)])
        diepte.append([default_diepte for i in range(aantal_kolomen_)])

    if (start_rij_ > y_): # kaart te klein (omhoog)
        start_rij_ -= 1
        aantal_rijen_ += 1
        kaart = [[default_teken for i in range(aantal_kolomen_)]] + kaart
        diepte = [[default_diepte for i in range(aantal_kolomen_)]] + diepte

    if (diepte[y_ - start_rij_][x_ - start_kolom_] <= z_): # enkel als voor vorige is
        kaart[y_ - start_rij_][x_ - start_kolom_] = teken
        diepte[y_ - start_rij_][x_ - start_kolom_] = z_

    z_ += 1 # verplaats voor volgende

    return kaart, diepte, x_, y_, z_, aantal_rijen_, aantal_kolomen_, start_rij_, start_kolom_

def westen(teken, kaart, diepte):
    aantal_rijen_, aantal_kolomen_ = aantal_rijen, aantal_kolomen
    start_rij_, start_kolom_ = start_rij, start_kolom
    x_, y_, z_ = x, y, z
    #print(aantal_rijen_, aantal_kolomen_)
    #print(start_rij_, start_kolom_)
    #print(x_, y_, z_)

    if (start_kolom_ > x_): # kaart te klein (vooraan)
        start_kolom_ -= 1
        aantal_kolomen_ += 1 # kolom toevoegen
        kaart = [[default_teken] + rij for rij in kaart]
        diepte = [[default_diepte] + rij for rij in diepte]
        
    if (aantal_rijen_ <= y_ - start_rij_): # kaart te klein (rijen)
        aantal_rijen_ += 1 # rij toevoegen
        kaart.append([default_teken for i in range(aantal_kolomen_)])
        diepte.append([default_diepte for i in range(aantal_kolomen_)])

    if (start_rij_ > y_): # kaart te klein (omhoog)
        start_rij_ -= 1
        aantal_rijen_ += 1
        kaart = [[default_teken for i in range(aantal_kolomen_)]] + kaart
        diepte = [[default_diepte for i in range(aantal_kolomen_)]] + diepte

    if (diepte[y_ - start_rij_][x_ - start_kolom_] <= z_): # enkel als voor vorige is
        kaart[y_ - start_rij_][x_ - start_kolom_] = teken
        diepte[y_ - start_rij_][x_ - start_kolom_] = z_

    x_ -= 1 # verplaats voor volgende

    return kaart, diepte, x_, y_, z_, aantal_rijen_, aantal_kolomen_, start_rij_, start_kolom_

def noorden(teken, kaart, diepte):
    aantal_rijen_, aantal_kolomen_ = aantal_rijen, aantal_kolomen
    start_rij_, start_kolom_ = start_rij, start_kolom
    x_, y_, z_ = x, y, z
    #print(aantal_rijen_, aantal_kolomen_)
    #print(start_rij_, start_kolom_)
    #print(x_, y_, z_)
        
    if (aantal_rijen_ <= y_ - start_rij_): # kaart te klein (rijen)
        #print('Kolom toevoegen')
        aantal_rijen_ += 1 # rij toevoegen
        kaart.append([default_teken for i in range(aantal_kolomen_)])
        diepte.append([default_diepte for i in range(aantal_kolomen_)])
        #print(kaart)

    if (start_rij_ > y_): # kaart te klein (omhoog)
        #print('Kolom toevoegen - omhoog')
        start_rij_ -= 1
        aantal_rijen_ += 1
        kaart = [[default_teken for i in range(aantal_kolomen_)]] + kaart
        diepte = [[default_diepte for i in range(aantal_kolomen_)]] + diepte
        #print(kaart)

    if (diepte[y_ - start_rij_][x_ - start_kolom_] <= z_): # enkel als voor vorige is
        kaart[y_ - start_rij_][x_ - start_kolom_] = teken
        diepte[y_ - start_rij_][x_ - start_kolom_] = z_

    z_ -= 1 # verplaats voor volgende

    return kaart, diepte, x_, y_, z_, aantal_rijen_, aantal_kolomen_, start_rij_, start_kolom_

for geval in range(1, aantal_testgevallen + 1):
    mes = input().split()
    aantal_segementen = mes[0]
    segementen = [segement for segement in str(mes[1])]

    #print(f'segementen: {segementen}')
    x, y, z = 0, 0, 0 # x: kolom, y: rij, z: diepte
    richting = 1 # 0: noorden, 1: oosten, 2: zuiden, 3:westen
    aantal_rijen, aantal_kolomen = 1, 0
    start_rij, start_kolom = 0, 0
    kaart = [[]]
    diepte = [[]]
    default_diepte = -124
    default_teken = '.'


    # algoritme
    for segement in segementen:
        #print('---------------')
        if (richting == 1): # oosten
            if (segement == 'S'):
                kaart, diepte, x, y, z, aantal_rijen, aantal_kolomen, start_rij, start_kolom = oosten('=', kaart, diepte)
                    
            elif (segement == 'V'):
                kaart, diepte, x, y, z, aantal_rijen, aantal_kolomen, start_rij, start_kolom = oosten('_', kaart, diepte)

            elif (segement == 'D'):
                y += 1
                kaart, diepte, x, y, z, aantal_rijen, aantal_kolomen, start_rij, start_kolom = oosten("\\", kaart, diepte)

            elif (segement == 'U'):
                kaart, diepte, x, y, z, aantal_rijen, aantal_kolomen, start_rij, start_kolom = oosten("/", kaart, diepte)
                y -= 1

            elif (segement == 'R'):
                kaart, diepte, x, y, z, aantal_rijen, aantal_kolomen, start_rij, start_kolom = oosten("_", kaart, diepte)
                z += 1
                x -= 1
                richting = 2

            elif (segement == 'L'):
                kaart, diepte, x, y, z, aantal_rijen, aantal_kolomen, start_rij, start_kolom = oosten("_", kaart, diepte)
                z -= 1
                x -= 1
                richting = 0


        elif (richting == 2): # zuiden
            if (segement == 'S'):
                kaart, diepte, x, y, z, aantal_rijen, aantal_kolomen, start_rij, start_kolom = zuiden('=', kaart, diepte)
                    
            elif (segement == 'V'):
                kaart, diepte, x, y, z, aantal_rijen, aantal_kolomen, start_rij, start_kolom = zuiden('_', kaart, diepte)

            elif (segement == 'D'):
                y += 1
                kaart, diepte, x, y, z, aantal_rijen, aantal_kolomen, start_rij, start_kolom = zuiden("#", kaart, diepte)

            elif (segement == 'U'):
                kaart, diepte, x, y, z, aantal_rijen, aantal_kolomen, start_rij, start_kolom = zuiden("#", kaart, diepte)
                y -= 1

            elif (segement == 'R'):
                kaart, diepte, x, y, z, aantal_rijen, aantal_kolomen, start_rij, start_kolom = zuiden("_", kaart, diepte)
                x -= 1
                z -= 1
                richting = 3

            elif (segement == 'L'):
                kaart, diepte, x, y, z, aantal_rijen, aantal_kolomen, start_rij, start_kolom = zuiden("_", kaart, diepte)
                x += 1
                z -= 1
                richting = 1

        elif (richting == 3): # westen
            if (segement == 'S'):
                kaart, diepte, x, y, z, aantal_rijen, aantal_kolomen, start_rij, start_kolom = westen('=', kaart, diepte)
                    
            elif (segement == 'V'):
                kaart, diepte, x, y, z, aantal_rijen, aantal_kolomen, start_rij, start_kolom = westen('_', kaart, diepte)

            elif (segement == 'D'):
                y += 1
                kaart, diepte, x, y, z, aantal_rijen, aantal_kolomen, start_rij, start_kolom = westen("/", kaart, diepte)

            elif (segement == 'U'):
                kaart, diepte, x, y, z, aantal_rijen, aantal_kolomen, start_rij, start_kolom = westen("\\", kaart, diepte)
                y -= 1

            elif (segement == 'R'):
                kaart, diepte, x, y, z, aantal_rijen, aantal_kolomen, start_rij, start_kolom = westen("_", kaart, diepte)
                z -= 1
                x += 1
                richting = 0

            elif (segement == 'L'):
                kaart, diepte, x, y, z, aantal_rijen, aantal_kolomen, start_rij, start_kolom = westen("_", kaart, diepte)
                z += 1
                x += 1
                richting = 2

        elif (richting == 0): # noorden
            if (segement == 'S'):
                kaart, diepte, x, y, z, aantal_rijen, aantal_kolomen, start_rij, start_kolom = noorden('=', kaart, diepte)
                    
            elif (segement == 'V'):
                kaart, diepte, x, y, z, aantal_rijen, aantal_kolomen, start_rij, start_kolom = noorden('_', kaart, diepte)

            elif (segement == 'D'):
                y += 1
                kaart, diepte, x, y, z, aantal_rijen, aantal_kolomen, start_rij, start_kolom = noorden("#", kaart, diepte)

            elif (segement == 'U'):
                kaart, diepte, x, y, z, aantal_rijen, aantal_kolomen, start_rij, start_kolom = noorden("#", kaart, diepte)
                y -= 1

            elif (segement == 'R'):
                kaart, diepte, x, y, z, aantal_rijen, aantal_kolomen, start_rij, start_kolom = noorden("_", kaart, diepte)
                x += 1
                z += 1
                richting = 1

            elif (segement == 'L'):
                kaart, diepte, x, y, z, aantal_rijen, aantal_kolomen, start_rij, start_kolom = noorden("_", kaart, diepte)
                x -= 1
                z += 1
                richting = 3

        #print(f'{segement}: {kaart}')
        #print(richting)

    #print(kaart)

    for rij in kaart:
        print(f'{geval} {"".join(rij)}')


