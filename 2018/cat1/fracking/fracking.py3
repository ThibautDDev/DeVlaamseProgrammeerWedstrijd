# check grond
def is_goed(grond):
    check = [a[:] for a in grond]
    algeweest = [ a[:] for a in check]

    for start_kolom in range(aantal_kolomen):
        if check[0][start_kolom] == '*':
            vorige_rij, vorige_kolom = 0, start_kolom
            check_rij, check_kolom = 0, start_kolom

            while not (check_rij == 0 and check[vorige_rij][vorige_kolom] == 'O'):
                # onder
                if check_rij != aantal_rijen - 1 and algeweest[check_rij + 1][check_kolom] == '*':
                    vorige_rij, check_rij = check_rij, check_rij + 1
                    vorige_kolom = check_kolom

                    aantal_terug = 0
                # links
                elif check_kolom != 0 and algeweest[check_rij][check_kolom - 1] == '*' and check_kolom - 1 != vorige_kolom:
                    vorige_kolom, check_kolom = check_kolom, check_kolom - 1
                    vorige_rij = check_rij

                    aantal_terug = 0
                # rechts
                elif check_kolom != aantal_kolomen - 1 and algeweest[check_rij][check_kolom + 1] == '*' and check_kolom + 1 != vorige_kolom:
                    vorige_kolom, check_kolom = check_kolom, check_kolom + 1
                    vorige_rij = check_rij

                    aantal_terug = 0
                # Terug omhoog
                elif check_rij != 0 and algeweest[check_rij - 1][check_kolom] == '*':
                    #check[check_rij][check_kolom] = 'O'
                    #algeweest[check_rij][check_kolom] = 'O'
                    vorige_rij, check_rij = check_rij, check_rij - 1
                    vorige_kolom = check_kolom
                    #aantal_terug += 1

                # algeweest check
                    # onder
                elif algeweest[check_rij + 1][check_kolom] == '1':
                    check[check_rij][check_kolom] = 'O'
                    algeweest[check_rij][check_kolom] = 'O'
                    vorige_rij, check_rij = check_rij, check_rij + 1
                    vorige_kolom = check_kolom

                    aantal_terug = 0
                    # links
                elif check_kolom != 0 and algeweest[check_rij][check_kolom - 1] == '1':
                    check[check_rij][check_kolom] = 'O'
                    algeweest[check_rij][check_kolom] = 'O'
                    vorige_kolom, check_kolom = check_kolom, check_kolom - 1
                    vorige_rij = check_rij

                    aantal_terug = 0
                    # rechts
                elif check_kolom != aantal_kolomen - 1 and algeweest[check_rij][check_kolom + 1] == '1':
                    check[check_rij][check_kolom] = 'O'
                    algeweest[check_rij][check_kolom] = 'O'
                    vorige_kolom, check_kolom = check_kolom, check_kolom + 1
                    vorige_rij = check_rij

                    aantal_terug = 0
                    # Terug omhoog
                elif algeweest[check_rij - 1][check_kolom] == '1':
                    check[check_rij][check_kolom] = 'O'
                    algeweest[check_rij][check_kolom] = 'O'
                    vorige_rij, check_rij = check_rij, check_rij - 1
                    vorige_kolom = check_kolom
                    #aantal_terug += 1

                else:
                    break


                algeweest[check_rij][check_kolom] = '1'

                if check_rij == aantal_rijen - 1:
                    return True
    return False


#---------- Programma ----------
aantal_testgevallen = int(input())
alle_testgevallen = []

for testgeval in range(1, aantal_testgevallen + 1):
    aantal_rijen = int(input())
    aantal_kolomen = int(input())

    grond = []

    aantal_dagen = 0

    for a in range(aantal_rijen):
        rij = []
        rij += input()
        grond.append(rij)

    while is_goed(grond):
        aantal_dagen += 1

        for rij in range(aantal_rijen):
            for kolom in range(aantal_kolomen):
                if grond[rij][kolom] == '.':
                    if kolom != 0 and grond[rij][kolom - 1] == '*':
                        grond[rij][kolom - 1] = 'O'
                    if kolom != aantal_kolomen - 1 and grond[rij][kolom + 1] == '*':
                        grond[rij][kolom + 1] = 'O'
                    if rij != 0 and grond[rij - 1][kolom] == '*':
                        grond[rij - 1][kolom] = 'O'
                    if rij != aantal_rijen - 1 and grond[rij + 1][kolom] == '*':
                        grond[rij + 1][kolom] = 'O'

        for rij in range(aantal_rijen):
            for kolom in range(aantal_kolomen):
                if grond[rij][kolom] == 'O':
                    grond[rij][kolom] = '.'

    print(testgeval, aantal_dagen)

