def checkNaomees(woord):
    lengte = len(woord)
    # print(lengte)
    if(lengte == 2 and (woord == "du" or woord == "ba" or woord == "di")):
        return True
    elif (lengte == 0):
        return True
    w1 = woord[:2]
    w2 = woord[-2:]
    # print(w1, w2, woord[2:-2])
    if(w1 == w2): return checkNaomees(woord[2:-2])
    else: return False


for testgeval in range(1, 1+int(input())):
    uitkomst = []
    for i in range(5):
        woord = input()
        output = checkNaomees(woord)
        # print(output)
        # print()
        if(output): uitkomst += ["naomees"]
        else: uitkomst += ["onzin"]

    print(f"{testgeval} {uitkomst[0]} {uitkomst[1]} {uitkomst[2]} {uitkomst[3]} {uitkomst[4]}")


'''
1
badudiba
didibabadidubadubabadubadidubadu
dudibadududuba
badiba
dibadi

onzin onzin onzin naomees naomees
'''

