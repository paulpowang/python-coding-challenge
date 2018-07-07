import math




def isPrime(num):
    '''
    if num <= 1:
        return False
    elif num ==2 or num ==3 or num == 5 or num == 7:
        return True
    elif num%2 == 0:
        return False
    else:
        for i in range(7, num, 2):
            if num%i == 0:
                return False
        return True
    '''
    if num <= 1:
        return False
    elif num ==2 or num ==3 or num == 5 or num == 7:
        return True
    elif num%2 == 0:
        return False
    else:
        sqrt_num = int(math.sqrt(num))
        for i in range(3, sqrt_num+1):
            if num%i == 0:
                return False
        return True
            
            

T = int(input())
for i in range(T):
    if isPrime(int(input())):
        print('Prime')
    else:
        print('Not prime')
