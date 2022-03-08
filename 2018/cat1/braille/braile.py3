def tekens(lijn1, lijn2, lijn3, i):
    return (lijn1[i:i+2]), (lijn2[i:i+2]), (lijn3[i:i+2])

alfabet = {}
letter = 65

lijn1 = input()
lijn2 = input()
lijn3 = input()

for i in range(0, len(lijn1), 2):
    teken = tekens(lijn1, lijn2, lijn3, i)
    alfabet[teken] = chr(letter)
    letter += 1

aantal_testgevallen = int(input())

for testgeval in range(1, aantal_testgevallen + 1):
    print(testgeval, end=' ')
    lijn1 = input()
    lijn2 = input()
    lijn3 = input()
    for i in range(0, len(lijn1), 2):
        print(alfabet[tekens(lijn1, lijn2, lijn3, i)], end='')
    print()
