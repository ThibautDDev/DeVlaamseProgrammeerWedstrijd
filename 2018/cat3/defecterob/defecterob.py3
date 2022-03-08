#Swapping mechanisme niet op punt. Voorbeeldinvoer werkt, wedstrijd invoer niet

def reOrderOutput(output):
    print(output)
    out = []

    temp = []
    for i in range(len(output)):
        temp += [output[i]]
        if len(temp) == 2:
            sorted(temp)
            try:
                if out[-1] == temp[0]:
                    out = out[:-1]
                    out += temp[1]
                else:
                    out += temp[0]
                    out += temp[1]
            except:
                out += temp[0]
                out += temp[1]

            temp = []

    print("out", out)
    return out


for testgeval in range(1, 1+int(input())):
    char = 65
    output = ""
    
    lijn = input("")
    buffer = [i for i in lijn]
    print(buffer)

    lijn = input("")
    correctie = [i for i in lijn]
    print(correctie)

    if buffer == correctie:
        output = "correct"
    
    else:
        try:
            i = 0
            j = 0
            while buffer != correctie:
                if buffer[i] != correctie[i]:
                    el1 = buffer[i]
                    el2 = buffer[j]
                    cor = correctie[i]
                    if el2 == cor:
                        buffer[i] = el2
                        buffer[j] = el1
                        output += chr(i+char)
                        output += chr(j+char)
                        j = i
                    else:
                        j += 1

                    if j == len(buffer):
                        i = 0
                        j = 0
                else:
                    i += 1
                    j = i
            #print("output gevonden")
            output = reOrderOutput(output)
        except:
            output = "onmogelijk"
    
    print(f"{testgeval} {output}")
    print()


"""
3
SLSLSR
SSLLRS
SS
RR
SSLLRR
SSLLRR

1
SSRRLLLLRLRLSLRSSSS
SSLRLLLLLLRRSSSRRSS
"""