aantal_testgevallen = int(input())

for testgeval in range(1, aantal_testgevallen + 1):
    saldo = int(input())
    invoer = input().split()
    aantal_bedragen = int(invoer[0])
    trasacties = [int(x) for x in invoer[1:]]
    trasacties.sort()
    for bedrag in range(aantal_bedragen):
        saldo += trasacties[bedrag]
        if saldo < 0:
            saldo -= 35
    print(testgeval, saldo)