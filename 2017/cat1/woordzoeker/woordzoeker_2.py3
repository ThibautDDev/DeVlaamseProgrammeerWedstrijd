from itertools import count


def convertHorizontalVertical(lst):
    raster = []
    for j in range(len(lst[0])):
        line = ""
        for i in range(len(lst)):
            line += lst[i][j]
        raster += [line]
    return raster

def convertHorizontalToDiagonal(lst, reverse=False):
    raster = []
    for i in range(len(lst)):
        symb1 = (len(lst)-1-i)*"@"  
        symb2 = (i)*"@"
        # print(symb1, symb2)
        if(reverse): raster += [f"{symb2}{lst[i]}{symb1}"]
        else: raster += [f"{symb1}{lst[i]}{symb2}"]
    return convertHorizontalVertical(raster)

def convertDiagonalToHorizontal(lst):
    raster = []
    for j in range(len(lst[0])):
        line = ""
        for i in range(len(lst)):
            line += lst[i][j]
        raster += [line.replace("@", "")]
    return raster

def checkForWords(lst, lstWords):
    raster = []
    for i in range(len(lst)):
        rij = lst[i]
        tocheck = []
        for woord in lstWords:
            if(rij.find(woord) != -1):
                # print(rij, woord)
                tocheck.append(rij.replace(woord, "#"*len(woord)))
            elif(rij.find(woord[::-1]) != -1):
                # print(rij, woord)
                tocheck.append(rij.replace(woord[::-1], "#"*len(woord)))
        for c in tocheck: 
            for j in range(len(c)):
                if(c[j] == "#"): rij = rij[:j] + "#" + rij[j+1:]
        raster.append(rij)
    # print(raster)
    return raster

for testgeval in range(1, 1 + int(input())):
    invoerLijn = input()
    aantal_woorden = int(invoerLijn.split(" ")[0])
    aantal_rijen = int(invoerLijn.split(" ")[1])
    aantal_kolommen = int(invoerLijn.split(" ")[2])
    # print(aantal_woorden, aantal_rijen, aantal_kolommen)
    woordenlijst = [input() for i in range(aantal_woorden)]
    
    
    raster = []
    for i in range(aantal_rijen): 
        raster += [input()]
    # print()

    # print()
    # print(raster)
    # vert = convertHorizontalVertical(raster)
    # print(vert)
    # print()
    # checkForWords(vert, woordenlijst)
    horizontal = checkForWords(raster, woordenlijst)
    vertical = convertHorizontalVertical(checkForWords(convertHorizontalVertical(raster), woordenlijst))
    diagonal1 = convertDiagonalToHorizontal(checkForWords(convertHorizontalToDiagonal(raster), woordenlijst))
    diagonal2 = convertDiagonalToHorizontal(checkForWords(convertHorizontalToDiagonal(raster, True), woordenlijst))

    # print(horizontal)
    # print(vertical)
    # print(diagonal1)
    # print(diagonal2)
    # print()
    # print(convertHorizontalToDiagonal(raster))

    result = ""
    for i in range(aantal_rijen):
        for j in range(aantal_kolommen):
            el1 = horizontal[i][j]
            el2 = vertical[i][j]
            el3 = diagonal1[i][j]
            el4 = diagonal2[i][j]
            
            # print(el1, el2, el3, el4)
            if(el1 == el2 and el2 == el3 and el3 == el4 and el4 != "#"): result += el1
    print(f"{testgeval}", result)

"""
1
10 12 10
algoritme
databank
software
hardware
programmeren
debuggen
klasse
object
compileren
moederbord
ndenmzeoef
eeneoingis
gdkreniete
galedzogmr
utameemtaa
basmrkiktw
ebsabrelcd
daeroijker
anlgrszeja
lklodijkbh
taerawtfos
compileren
"""



"""
1
17 17 14
grzpav
rcvvlf
dvztn
kjbsi
ulkxu
lfembe
bisbjk
flvvcr
hblfcm
grzpa
zkfjg
kmjttz
patroms
gndbol
uzkfjg
gmuafqz
besnza
hvrjaffbkpgzzs
iadtvrllprpujb
pnilmgzejzldve
ewpnrosbuektai
ajnhqczqxupfho
idcsvmxiwlrfbe
xxttbrgnnveerz
mhwdvayhoknmth
auihpivscapmub
pjblthxzqfaumg
fzcrknmacxrxqi
znuvbumaelsmyv
tazliucdbesnza
tekesxfsmortap
jifbbklxerdzuz
mvjbjlbjflvvcr
khgskuhflobdng
"""