import itertools

def vulIn(vgl, combi):
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    for i in range(len(combi)):
        num = combi[i]
        letter = letters[i]
        vgl = vgl.replace(letter, num)

    #print(eval(vgl))
    return vgl


def opmaak(vgl):
    retVgl = ""
    haakje = False
    for i in range(len(vgl)-1):
        item = vgl[i]
        item2= vgl[i+1]
        #print(i, len(vgl), item, item2)
        if haakje == False and (item2 == "*" or item2 == ":"):
            haakje = True
            retVgl += "("
            retVgl += item
        elif haakje == True and (item2 == "+" or item2 == "-"):
            haakje = False
            retVgl += item
            retVgl += ")"
        else:
            retVgl += item

    #laatste getal toevoegen wat de loop overslaat door len()-1
    retVgl += item2
    if haakje:
        retVgl += ")"

    #Gedeeld door tekens vervangen voor syntax
    retVgl = retVgl.replace(":", "/")
    #print(retVgl)
    return retVgl


def checkGeheleGetallen(vgl):
    bew = ""
    add = False
    for i in range(len(vgl)):
        if add:
            bew += vgl[i]

        if vgl[i] == "(":
            add = True
        elif vgl[i] == ")":
            add = False
            bew = bew[:-1]
            calc = eval(bew)
            #print(calc%1)
            if "float" in str(type(calc)) and not calc.is_integer():
                return False
            bew = ""
    return True


def genOutput(combi):
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    val = ""
    for i in range(len(combi)):
        val += f"{letters[i]}={combi[i]} "

    #laatste spatie eraf
    val = val[:-1]
    return val


for testgeval in range(1, 1 + int(input(""))):
    lijn = input().split(" ")
    mogelijkeGetallen = [str(i) for i in lijn]
    #print(mogelijkeGetallen)

    vergelijking = input().split(" ")
    uitkomst = int(vergelijking[-1])
    vergelijking = vergelijking[:-2]
    #print()
    #print(vergelijking)

    vergelijking = opmaak(vergelijking)
    #print(vergelijking)

    #print(losOp(vergelijking, uitkomst, mogelijkeGetallen))
    combinaties = list(itertools.permutations(mogelijkeGetallen))
    for combi in combinaties:
        vgl = vulIn(vergelijking, combi)
        if checkGeheleGetallen(vgl) == True and eval(vgl) == uitkomst:
            output = genOutput(combi)
            print(testgeval, output)


    #print()
    #print("-"*30)
    #print()