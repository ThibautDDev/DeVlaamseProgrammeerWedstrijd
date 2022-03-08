aantal_testgevallen = int(input())

for testgeval in range(1, aantal_testgevallen + 1):
    getal = int(input())
    getallen = []
    while getal >= 0:
        getallen.append(getal)
        getal = int(input())
    m = max(getallen)
    n = len(getallen)
    print(testgeval, int(round(((n + 1) * m / n - 1), 0)))
    