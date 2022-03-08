aantal_testgevallen = int(input())

for testgeval in range(1, aantal_testgevallen + 1):
    info = input().split()
    aantal_rijen = int(info[0])
    aantal_kolomen = int(info[1])
    info  = input().split()
    aantal_kruispunten = int(info[0])
    info.pop(0)
    kruispunten = [[int(info[i]) - 1, int(info[i + 1]) - 1] for i in range(0,aantal_kruispunten * 2, 2)]
    raam = [['.' for kolom in range(aantal_kolomen)] for rij in range(aantal_rijen)]

    for kruis in kruispunten:
        rij, kolom = kruis[0], kruis[1]
        raam[rij][kolom] = '*'
        # omhoog
        while rij != 0 and raam[rij - 1][kolom] != '*':
            rij -= 1
            raam[rij][kolom] = '*'
        # omlaag
        rij, kolom = kruis[0], kruis[1]
        while rij != aantal_rijen - 1 and raam[rij + 1][kolom] != '*':
            rij += 1
            raam[rij][kolom] = '*'
        # links
        rij, kolom = kruis[0], kruis[1]
        while kolom != 0 and raam[rij][kolom - 1] != '*':
            kolom -= 1
            raam[rij][kolom] = '*'
        # recht
        rij, kolom = kruis[0], kruis[1]
        while kolom != aantal_kolomen - 1 and raam[rij][kolom + 1] != '*':
            kolom += 1
            raam[rij][kolom] = '*'

    for rij in range(aantal_rijen):
        print(testgeval, end=' ')
        for element in raam[rij]:
            print(element, end='')
        print()