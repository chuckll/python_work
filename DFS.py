# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 16:20:23 2018

@author: chuck
"""

map_array = [ [0,0,0,0,0,0,0,0],
              [0,1,1,1,1,0,1,0],
              [0,0,0,0,1,0,1,0],
              [0,1,0,0,0,0,1,0],
              [0,1,0,1,1,0,1,0],
              [0,1,0,0,0,0,1,1],
              [0,1,0,0,1,0,0,0],
              [0,1,1,1,1,1,1,0]  ]

res = []

class node:                                   #定义位置结点类    
    def __init__(self, x, y):
        self.x =x
        self.y=y

def dfs(x, y):
    cur = node(x, y)
    res.append(cur)
    if x == 7 and y == 7:                  #走到出口
        print(len(res))
        for i in range(len(res)):
            print(" (" + str(res[i].x)+ "," + str(res[i].y) + ")" , end="--")
        print("")
        return True
    if x == 8 or x == -1 or y == 8 or y == -1 or map_array[x][y] == 1:     #超出范围或遇到墙
        return False
    map_array[x][y] = 1
    if dfs(x+1, y):              #向右走
        return
    if dfs(x-1, y):             #向左走
        return
    if dfs(x, y+1):            #向下走
        return
    if dfs(x, y-1):           #向上走
        return
    map_array[x][y] = 0
    res.pop()
    
dfs(0,0)