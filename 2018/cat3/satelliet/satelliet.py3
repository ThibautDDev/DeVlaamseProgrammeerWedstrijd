#Hoe lijst efficient overlopen?
for testgeval in range(1, 1+int(input())):
    code = input("")
    
    db = []
    for i in range(int(input())):
        lijn = []
        for j in range(2):
            lijn += [input()]
        db += [lijn]
    print(db)
    db = sorted(db, key=lambda x: len(x[1]), reverse=True)
    print(db)

    



"""
2
0110
3
Q
01
S
011
P
10
0011011011000
3
Q
01
S
011
P
10
"""