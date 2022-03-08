# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 12:49:23 2021

@author: louis
"""

def main():
    testgevallen = int(input())
    for testgeval in range(testgevallen):
        K, V = input().rstrip().split()
        knooppunten = [[i+1, 1, 9999] for i in range(int(K))]
        knooppunten[0][2] = 0
        knooppunten[0][1] = 0
        verbindingen = []
        for _ in range(int(V)):
            start, stop, strafpunten = input().rstrip().split()
            verbindingen.append([int(start), int(stop), int(strafpunten)])
        waarde = zoekWeg(knooppunten, verbindingen)
        
        print(str(testgeval+1) + " " + str(waarde))
        

#knooppunten = [[knooppunt, overlopen?, waarde]]
#verbindingen = [start, stop, kost]

def zoekWeg(knooppunten, verbindingen):
    for knooppunt in knooppunten:
        if knooppunt[2] < -1000:
            return "min oneindig"
    
    for knooppunt in knooppunten:
        if knooppunt[1] == 0:
            for verbinding in verbindingen:
                if verbinding[0] == knooppunt[0]:
                    if knooppunten[verbinding[1]-1][2] > verbinding[2] + knooppunt[2]:
                        knooppunten[verbinding[1]-1][2] = verbinding[2] + knooppunt[2]
                        knooppunten[verbinding[1]-1][1] = 0  

            knooppunt[1] = 1       
                            
    for knooppunt in knooppunten:                                
        if knooppunt[1] == 0:
            return zoekWeg(knooppunten, verbindingen)
            break

    

        
    
    if knooppunten[-1][2] == 9999:
        return "plus oneindig"
    return knooppunten[-1][2]
            




main()
            