#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    
    email_list = []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        email_list.append([firstName, emailID])
    #set pattern
    email_pattern = '@gmail.com'
    email_name_list = []
    for i in range(len(email_list)):
        if email_pattern in email_list[i][1]:
            email_name_list.append(email_list[i][0])
    new_list = email_name_list.sort()
    for i in range(len(email_name_list)):
        print(email_name_list[i])