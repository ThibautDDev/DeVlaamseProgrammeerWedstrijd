aantal_testgevallen = int(input())

for testgeval in range(1, aantal_testgevallen + 1):
    aantal_meetingen = int(input())
    afstand = 0
    x2, y2 = 0, 0
    for meeting in range(aantal_meetingen):
        positie = input().split(' ')
        x1 = int(positie[0])
        y1 = int(positie[1])
        # formule d = |x2 − x1| + |y2 − y1|
        afstand += abs(x2 - x1) + abs(y2 - y1)
        x2, y2 = x1, y1
    print(testgeval,afstand)