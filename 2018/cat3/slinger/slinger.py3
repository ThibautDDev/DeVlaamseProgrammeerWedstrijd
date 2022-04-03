testgevallen = int(input())

def split(word):
    return [char for char in word]

def largestNumber(in_str):
    l=[int(x) for x in split(in_str) if x.isdigit()]
    # print(l)
    return max(l) if l else 0


for testgeval in range(1, 1+testgevallen):
    # print()
    slingerLengte = int(input())
    slinger = input()

    slingerShort = ""
    count = 0
    stop = False
    for i in range(slingerLengte-1):
        symbol = slinger[i]
        if(slinger[i+1] == symbol and symbol == "*"): 
            slinger = slinger[0:i+1] + "." + slinger[i+2:]
            stop = True
            break
        if(symbol == "."):
            count += 1
        if(symbol == "*" and count > 0):
            slingerShort += f"{count}*"
            count = 0
        elif(symbol == "*"):
            slingerShort += "*"
    
    if(stop): print(f"{testgeval} {slinger}")
    else:
        maxNumber = largestNumber(slingerShort)
        recurrence, pattern = 0, 0
        for i in range(1, maxNumber):
            rec = slingerShort.count(str(i))
            if(rec > recurrence):
                recurrence = rec
                pattern = i
        if(recurrence == pattern and pattern == 0 or maxNumber < pattern): print(f"{testgeval} {slinger}")
        else:
            # print(maxNumber, pattern)
            slinger2 = ""
            for i in range(len(slingerShort)):
                if(slingerShort[i] != "*" and int(slingerShort[i]) > pattern and i == 0):
                    if(int(slingerShort[i]) -1 == pattern):
                        slinger2 += "*"
                        slinger2 += "."*pattern
                    else:
                        slinger2 += "."*((maxNumber-1)//2)
                        slinger2 += "*"
                        slinger2 += "."*((maxNumber-1)//2)
                elif(slingerShort[i] != "*" and int(slingerShort[i]) > pattern):
                    slinger2 += "."*((int(slingerShort[i]) - 1)//2)
                    slinger2 += "*"
                    slinger2 += "."*((int(slingerShort[i]) - 1)//2)
                elif(slingerShort[i] != "*"):
                    slinger2 += "."*int(slingerShort[i])
                else: 
                    slinger2 += "*"
            print(f"{testgeval} {slinger2}")
                    
        
    



"""
6
20
***.*.*.*.*.*.*.*.*.
20
*.*.*.***.*.*.*.*.*.
21
.*.*.*.*.*...*.*.*.*.
22
*.*...*.*.*.*.*.*.*.*.
22
.*.*.*.*.*.*.*.*.*.*.*
21
.*..*..*..*.....*..*.
"""