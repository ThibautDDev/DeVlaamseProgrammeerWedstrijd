###Foutieve versie van xander


def checkNaomees(woord):
    lengte = len(woord)
    if lengte % 4 != 0:
        return False
    w1 = woord[:lengte//2]
    w2 = woord[lengte//2:]
    print("w1", w1)
    print("w2", w2)
    gespiegeld = ''.join([woord[i:i+2] for i in range(lengte//2-2, -1, -2)])
    print('gege', woord)
    print('spie', gespiegeld)
    # 'bi bu ba ba bu bi'
    # ba bu bi


for testgeval in range(1, 1+int(input())):
    uitkomst = []
    for i in range(5):
        woord = input()
        output = checkNaomees(woord)
        print()
        # print(output)
        # print()
        if(output): uitkomst += ["naomees"]
        else: uitkomst += ["onzin"]

    print(f"{testgeval} {uitkomst[0]} {uitkomst[1]} {uitkomst[2]} {uitkomst[3]} {uitkomst[4]}")


'''
1
dudubabadudubabadudu
didudubadududi
dudubadibadibadu
dididudidibadibadididudidi
babadidudidibadi
'''