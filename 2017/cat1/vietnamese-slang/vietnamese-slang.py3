import itertools

def vulIn(vglLst, combi):
    vgl = "".join(vglLst)
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    for i in range(len(combi)):
        num = combi[i]
        letter = letters[i]
        vgl = vgl.replace(letter, num)
    return vgl

def genOutput(combi):
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    val = ""
    for i in range(len(combi)):
        val += f"{letters[i]}={combi[i]} "
    val = val[:-1]
    return val


testgevallen = int(input())
for testgeval in range(1, 1 + testgevallen):
    mogelijkeGetallen = [str(i) for i in input().split(" ")]
    vergelijking = input()
    uitkomst = int(vergelijking.split(" ")[-1])
    vergelijking = vergelijking.replace(":", "/").split(" ")[:-2]
    # print()
    # print(mogelijkeGetallen)
    # print(vergelijking)

    permutaties = list(itertools.permutations(mogelijkeGetallen))
    for combi in permutaties:
        vgl = vulIn(vergelijking, combi)
        if eval(vgl) == uitkomst:
            output = genOutput(combi)
            print(testgeval, output)

"""
1
1 2 3 4 5 6 7 8 9
A + 13 * B : C + D + 12 * E - F - 11 + G * H : I - 10 = 66
"""