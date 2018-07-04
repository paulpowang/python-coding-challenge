#!/bin/python3

import math

##### My Code Here ####
def get_maxmun_sum(arr):
    max_sum = -(math.inf)
    for i in range(len(arr)-2):
        for j in range(len(arr[i])-2):
            
            a = arr[i][j]
            b = arr[i][j+1]
            c = arr[i][j+2]
            d= arr[i+1][j+1]
            e= arr[i+2][j]
            f = arr[i+2][j+1] 
            g = arr[i+2][j+2]
            sum = a + b + c + d + e + f + g
                       
            if sum > max_sum:
                max_sum = sum
                
    print(max_sum)
#### My Code End Here ###


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
    get_maxmun_sum(arr)