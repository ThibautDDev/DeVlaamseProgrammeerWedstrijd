testgevallen = int(input())

def checkIfPossible(snoepjes):
    count = 0
    for snoep in snoepjes:
        count += snoep
    # print(count, len(snoepjes))
    if count % len(snoepjes) != 0:
        return False
    return True

def correct(snoepjes):
    count = snoepjes[0]
    for i in range(1, len(snoepjes)):
        if count != snoepjes[i]: return False
    return True

for testgeval in range(1, 1+testgevallen):
    snoepjes = [int(i) for i in input().split(" ")[1:]]
    # print("snoepjes", snoepjes)
    if(not checkIfPossible(snoepjes)): print(f"{testgeval} ONEINDIG")
    else:
        count = 0
        while not correct(snoepjes):
            snoepjes1 = [i for i in snoepjes]
            count += 1
            for i in range(len(snoepjes)-1):
                if snoepjes[i] > snoepjes[i+1]:
                    snoepjes1[i] -= 1
                    snoepjes1[i+1] += 1
            if(snoepjes[-1] > snoepjes[0]):
                snoepjes1[-1] -= 1
                snoepjes1[0] += 1
            # print(snoepjes)
            # print(snoepjes1)
            # print()
            snoepjes = snoepjes1

        print(f"{testgeval} {count}")
    # print()
    # print()

"""
C:/Users/thiba/Documents/GithubRepos/DeVlaamseProgrammeerWedstrijd/2021/cat3/snoepjes/snoepjes.py3
4
2 5 5
2 1 3
3 3 6 9
4 3 4 4 4

"""