testgevallen = int(input())

def aantalJuisteCijfers(gok, lst):
    aantal = 0
    for i in range(6):
        if(gok[i] in lst[:6]): aantal += 1
    return aantal

for testgeval in range(1, 1+testgevallen):
    getrokkenGetallen = [int(i) for i in input().split(" ")]
    # print(getrokkenGetallen)

    aantalGokken = int(input())
    gokken = [[int(i) for i in input().split(" ")] for j in range(aantalGokken)]
    prijs = 0
    for gok in gokken:
        aantalJCijfers = aantalJuisteCijfers(gok, getrokkenGetallen)
        # print("AantalJuisteCijfers", aantalJCijfers)
        if(aantalJCijfers == 6): prijs += 1000000
        elif(aantalJCijfers == 5 and getrokkenGetallen[6] in gok): prijs += 35722
        elif(aantalJCijfers == 5): prijs += 1201
        elif(aantalJCijfers == 4 and getrokkenGetallen[6] in gok): prijs += 218
        elif(aantalJCijfers == 4): prijs += 22
        elif(aantalJCijfers == 3 and getrokkenGetallen[6] in gok): prijs += 8
        elif(aantalJCijfers == 3): prijs += 5
        elif(aantalJCijfers == 2 and getrokkenGetallen[6] in gok): prijs += 3
    print(f"{testgeval}", prijs)

"""
1
38 35 27 26 24 40 3
13
3 24 26 35 38 40
24 26 27 35 38 40
3 24 26 35 38 40
26 35 37 38 44 45
2 3 15 20 30 38
3 26 27 35 38 40
3 24 26 35 38 40
3 30 32 35 38 40
3 24 26 27 35 38
8 14 24 26 27 43
3 24 26 27 38 41
3 14 26 35 40 44
1 18 20 26 27 38
"""