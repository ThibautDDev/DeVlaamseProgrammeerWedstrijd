def isIntersecting(circleNr, getal, crdx, crdy, asgn):
    radiusCircleNr = sum(asgn[circleNr]) + getal
    for circle in range(len(crdx)):
        if circleNr != circle:
            radiusSum = sum(asgn[circle]) + radiusCircleNr
            #xdiff = abs(crdx[circle] - crdx[circleNr]) 
            #ydiff = abs(crdy[circle] - crdy[circleNr]) 
                    
            distance = distancematrix[circle][circleNr]
            if distance <= radiusSum**2:
                return True
    return False

def getTotalScore(assignments):
    total = 0
    for circle in assignments:
        total += sum(circle) * len(circle)
    return total


def getNewScore(previousScore, getal, circle, asgn):
    return  previousScore + sum(asgn[circle]) + getal * (len(asgn[circle])+1)
                


def doAssignments2(asgn, getallen, i, previousScore):
    getal = getallen[i]
    possibleAssignments = []
    bestIntersectingScore = -1
    bestIntersectingCircle = -1
    
    for circle in range(c):
        newScore = (sum(asgn[circle])+getal) * (len(asgn[circle])+1)
            
        if newScore > bestIntersectingScore:
            bestIntersectingScore = newScore
            bestIntersectingCircle = circle
            
        if not isIntersecting(circle, getal, crdx, crdy, asgn):
            possibleAssignments.append(circle)
    
    intersectingTotal = getNewScore(previousScore, getal, bestIntersectingCircle, asgn)
    if len(possibleAssignments) == 0:
        return intersectingTotal
    
    bestScore = -1
    for asignment in possibleAssignments:

        if i+1 == len(getallen):
            newScore = getNewScore(previousScore, getal, asignment, asgn)
        else:
            asgnScore = getNewScore(previousScore, getal, asignment, asgn)
            asgn[asignment].append(getal)
            newScore = doAssignments2(asgn, getallen, i+1, asgnScore)
            asgn[asignment].pop(-1)
        bestScore = max(newScore, bestScore)
        
    return max(bestScore, bestIntersectingScore)


def doAssignments(asgn, getallen, i):
    getal = getallen[i]
    possibleAssignments = []
    bestIntersectingScore = -1
    bestIntersectingCircle = -1
    
    for circle in range(c):
        newScore = (sum(asgn[circle])+getal) * (len(asgn[circle])+1)
            
        if newScore > bestIntersectingScore:
            bestIntersectingScore = newScore
            bestIntersectingCircle = circle
            
        if not isIntersecting(circle, getal, crdx, crdy, asgn):
            possibleAssignments.append(circle)
    
    asgn[bestIntersectingCircle].append(getal)
    intersectingTotal = getTotalScore(asgn)
    asgn[bestIntersectingCircle].pop(-1)
    if len(possibleAssignments) == 0:
        return intersectingTotal
    
    bestScore = -1
    for asignment in possibleAssignments:
        asgn[asignment].append(getal)
        if i+1 == len(getallen):
            newScore = getTotalScore(asgn)
        else:
            newScore = doAssignments(asgn, getallen, i+1)
        asgn[asignment].pop(-1)
        bestScore = max(newScore, bestScore)
        
    return max(bestScore, bestIntersectingScore)
    
    
'''
with open("in.txt", 'r')  as file:
    with open("out.txt", 'r')  as check:
        n = int(file.readline())
    
        for opgavenr in range(n):
            cirkels, getallen = file.readline().split()
            c = int(cirkels)
            g = int(getallen)
            
        
            
            coords = file.readline().split()
            coords = [int(getal) for getal in coords]
            parity = True
            crdx = []
            crdy = []
            for getal in coords:
                if parity:
                    crdx.append(getal) 
                    parity = False
                else:
                    crdy.append(getal)
                    parity = True
            
            getallen = file.readline().split()
            getallen = [int(getal) for getal in getallen]
            
        
            # asgn = [ [getallenc1] , [getallenc2] , ...]
            asgn = [[] for _ in range(c)]
            
            distancematrix = [[] for _ in range(c)]
                
            for c1 in range(c):
                for c2 in range(c):
                    distancematrix[c1].append((crdx[c1] - crdx[c2])**2 + (crdy[c1] - crdy[c2])**2)
            
            # distance c1,c2 = distancematrix[c1][c2]
            
            bestScore = doAssignments2(asgn, getallen, 0, 0)
            
            if check.readline().rstrip() == f'{opgavenr+1} {bestScore}':
                print( f'{opgavenr+1} {bestScore} CORRECT')
            else:
                print( f'{opgavenr+1} {bestScore} FOUT')

'''

n = int(input())

for opgavenr in range(n):
    cirkels, getallen = input().split()
    c = int(cirkels)
    g = int(getallen)
    

    
    coords = input().split()
    coords = [int(getal) for getal in coords]
    parity = True
    crdx = []
    crdy = []
    for getal in coords:
        if parity:
            crdx.append(getal) 
            parity = False
        else:
            crdy.append(getal)
            parity = True
    
    getallen = input().split()
    getallen = [int(getal) for getal in getallen]
    

    # asgn = [ [getallenc1] , [getallenc2] , ...]
    asgn = [[] for _ in range(c)]
    
    distancematrix = [[] for _ in range(c)]
        
    for c1 in range(c):
        for c2 in range(c):
            distancematrix[c1].append((crdx[c1] - crdx[c2])**2 + (crdy[c1] - crdy[c2])**2)
    
    # distance c1,c2 = distancematrix[c1][c2]
    
    bestScore = doAssignments2(asgn, getallen, 0, 0)
    print(f'{opgavenr+1} {bestScore}')



'''
c = 6
g = 12
crdx = [1,14,7,20,6,50]
crdy = [1,4,5,10,20,20]
getallen = [5,2,1,8,4,4,14,2,8,7,14,10]
asgn = [[] for _ in range(c)]
bestScore = doAssignments2(asgn, getallen, 0,0)
print(f'{1} {bestScore}')


'''