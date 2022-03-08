aantal_testgevallen = int(input())

for testgeval in range(1, aantal_testgevallen + 1):
    info = input().split(' ')
    a = int(info[0])
    v = int(info[1])
    u = int(info[2])
    gevechtskracht = max(10, int(a * pow(v, 1/2) * pow(u, 1/2) * pow(0.7903, 2) / 10))
    print(testgeval, gevechtskracht)