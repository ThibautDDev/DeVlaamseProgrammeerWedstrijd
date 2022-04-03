#print(maakCode([[0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 1, 0, 0, 0]]))

def main():
    testgevallen = int(input())
    for testgeval in range(testgevallen):
        R, K = input().rstrip().split()
        matrix = []
        for _ in range(int(R)):
            rijRaw = input().rstrip()
            rij = []
            for char in rijRaw:
                if char == ".":
                    rij.append(0)
                else:
                    rij.append(1)
            matrix.append(rij)
        code = maakCode(matrix)
        
        print(str(testgeval+1)+" <"+str(R)+","+ str(K) +">" + str(code))
        
      
    
      
def maakCode(matrix, start= [0,0]):
    snijkolom = -1
    snijrij = -1
    for index, element in enumerate(matrix[0]):
        if element == 1:
            for index2, rij in enumerate(matrix):
                if rij[index] != 1:
                    break
                if index2 == len(matrix)-1:
                    snijkolom = index
                    
    
    for index, rij in enumerate(matrix):
        for index2, element in enumerate(rij):
            if element != 1:
                break
            if index2 == len(rij)-1:
                snijrij = index

    if snijrij != -1:
        
        rijen = []
        for index, rij in enumerate(matrix):
            if index < snijrij:
                rijen.append(rij)
                
        newrijen = []
        for rij in rijen:
            newrij = []
            for index, element in enumerate(rij):
                if index < snijkolom:
                    newrij.append(element)
            newrijen.append(newrij)
        
        LBMatrix = newrijen
        startLB = [0 + start[0],0 + start[1]]
        
        
        
        
        rijen = []
        for index, rij in enumerate(matrix):
            if index > snijrij:
                rijen.append(rij)
                
        newrijen = []
        for rij in rijen:
            newrij = []
            for index, element in enumerate(rij):
                if index < snijkolom:
                    newrij.append(element)
            newrijen.append(newrij)
        
        LOMatrix = newrijen
        startLO = [snijrij+1 + start[0],0 + start[1]]
        
        
        
        
        rijen = []
        for index, rij in enumerate(matrix):
            if index < snijrij:
                rijen.append(rij)
                
        newrijen = []
        for rij in rijen:
            newrij = []
            for index, element in enumerate(rij):
                if index > snijkolom:
                    newrij.append(element)
            newrijen.append(newrij)
                
        RBMatrix = newrijen
        startRB = [0 + start[0],snijkolom+1 + start[1]]
        
        
        
        
        rijen = []
        for index, rij in enumerate(matrix):
            if index > snijrij:
                rijen.append(rij)
        newrijen = []
        for rij in rijen:
            newrij = []
            for index, element in enumerate(rij):
                if index > snijkolom:
                    newrij.append(element)
            newrijen.append(newrij)    
        ROMatrix = newrijen
        startRO = [snijrij+1 + start[0],snijkolom+1 + start[1]]
        
        
        

        return "(" + str(snijrij + start[0] +1) + "," + str(snijkolom + start[1]+1) + ")["  + str(maakCode(LBMatrix,  startLB)) + "][" + str(maakCode(RBMatrix, startRB)) + "][" + str(maakCode(LOMatrix, startLO)) + "][" + str(maakCode(ROMatrix, startRO)) + "]"                                  
    else:
        return ""
             

main()