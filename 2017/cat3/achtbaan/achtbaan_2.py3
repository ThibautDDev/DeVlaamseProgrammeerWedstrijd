# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 17:20:20 2022

@author: louis
"""

# SSSSSVVUUUUVVDDDDUULVLVVVVVVVVVVVVUUUVVVDDDVVVLDDVLVVVVLVR
n = int(input())

# N O Z W
symbolconversion=[{'V':'_', 'U': '#', 'D': '#', 'L':'_','R':'_'},
                  {'S': '=','V':'_' , 'U': '/' , 'D': "\\", 'L':'_','R':'_'},
                  {'V':'_', 'U': '#', 'D': '#', 'L':'_','R':'_'},
                  {'V':'_' , 'U': "\\" , 'D': '/', 'L':'_','R':'_'}]

def updateMatrix(x,y,resultmatrix, depth):
    if x < 0:
        for row in resultmatrix:
            row.insert(0,'.')
        for row in depth:
            row.insert(0, -999)
        x += 1
        
    elif x > len(resultmatrix[0])-1:
        for row in resultmatrix:
            row.append('.')
        for row in depth:
            row.append(-999)
    
    
    if y < 0:
        resultmatrix.insert(0,['.' for _ in range(len(resultmatrix[0]))])
        depth.insert(0,[-999 for _ in range(len(resultmatrix[0]))])
        y += 1
          
        
    
    elif y > len(resultmatrix)-1:
        resultmatrix.append(['.' for _ in range(len(resultmatrix[0]))])
        depth.append([-999 for _ in range(len(resultmatrix[0]))])
            
    return x,y, resultmatrix, depth

for opgavenr in range(n):
    segmenten, string = input().split()
    resultmatrix = [['.']]
    depth = [[-999]]
    direct = 1
    c = 0
    x = 0
    y = 0
    
    # N O Z W
    for char in string:            
        if char == "D":
            y += 1
            
        
        x,y, resultmatrix, depth = updateMatrix(x,y,resultmatrix, depth)   
        
        if depth[y][x] < c:
            resultmatrix[y][x] = symbolconversion[direct][char]
            depth[y][x] = c
        
        if char == "U":
            y -= 1
            
        if char == 'L':
            direct = (direct-1)%4
        if char == 'R':
            direct = (direct+1)%4
        
        if direct == 1:
            x += 1
        
        if direct == 3:
            x -= 1
            
        if direct == 2:
            c += 1
        
        if direct == 0:
            c -= 1
        
    
    for line in resultmatrix:
        string = ''
        for char in line:
            string += char
        print(f'{opgavenr+1} {string}')