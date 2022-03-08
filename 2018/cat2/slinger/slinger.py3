aantal_testgevallen = int(input())

for testgeval in range(1, aantal_testgevallen + 1):
    lengte = int(input())
    slinger = []
    slinger += input()

# Tussenafstand
    puntjes, lengtes = 0, {}
    for i in range(lengte):
        if slinger[i] == '*' and str(puntjes) in lengtes:
            lengtes[str(puntjes)] += 'a'
            puntjes = 0
        elif slinger[i] == '*':
            lengtes[str(puntjes)] = 'a'
            puntjes = 0
        else:
            puntjes += 1
    for key, value in lengtes.items():
        if len(value) == max([len(x) for x in lengtes.values()]):
            afstand = int(key)
    print(afstand)

# Overlopen (ster te kort)
    puntjes, eerste = 0, ''.join(slinger).find('*') + 1
    for i in range(eerste, lengte):
        if slinger[i] == '.':
            puntjes += 1
        else:
            puntjes = 0
        if puntjes > afstand:
            slinger[i] = '*'
            puntjes = 0

    print(''.join(slinger))

    puntjes, eerste = 0, ''.join(slinger[::-1]).find('*')
    for i in range(-eerste, -lengte - 1, -1):
        if slinger[i] == '.':
            puntjes += 1
        else:
            puntjes = 0
        if puntjes > afstand:
            slinger[i] = '*'
            puntjes = 0

    print(''.join(slinger))

# Overlopen (punt te kort)
    puntjes, eerste = 0, ''.join(slinger).find('*') + 1
    for i in range(eerste, lengte):
        if slinger[i] == '.':
            puntjes += 1
        elif puntjes + 1 <= afstand:
            slinger[i] = '.'
            puntjes += 1
        else:
            puntjes = 0

    print(''.join(slinger))


    print(testgeval, ''.join(slinger))