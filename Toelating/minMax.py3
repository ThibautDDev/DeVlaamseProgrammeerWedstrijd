
aantal_gevallen = int(input())

for geval in range(1, aantal_gevallen + 1):
    lijst  = [int(input()) for i in range(int(input()))]
    print(f'{geval} {min(lijst)} {max(lijst)}')