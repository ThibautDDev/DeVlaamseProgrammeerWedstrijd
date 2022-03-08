# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 00:17:33 2021

@author: louis
"""
def main():
    testgevallen = int(input())
    for testgeval in range(testgevallen):
        scherm, A, O = input().rstrip().split()
        apps = input().rstrip().split()
        for i in range(len(apps)):
            apps[i] = int(apps[i])
        oproepen = input().rstrip().split()
        for i in range(len(oproepen)):
            oproepen[i] = int(oproepen[i])
        
        aantal = Tel(int(scherm), apps, oproepen)
        print(str(testgeval+1) + ' ' + str(aantal))
        
def Tel(scherm, apps, oproepen):
    teller = 0
    for oproep in oproepen:
        index = apps.index(oproep)
        if ((index+1)//scherm)*scherm == index+1:
            teller += ((index+1)//scherm)-1
        else:
            teller +=(index+1)//scherm
        if index != 0:
            temp = apps[index]
            apps[index] = apps[index-1]
            apps[index-1] = temp
    return teller

main()