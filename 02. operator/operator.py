#!/bin/python3




# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    ############ My code Start #############
    tip_percent = (tip_percent/100)*meal_cost
    tax_percent = (tax_percent/100)*meal_cost
    total_cost = meal_cost + tip_percent + tax_percent
    total_cost = round(total_cost)
    
    result = 'The total meal cost is ' + str(total_cost) + ' dollars.'
    print(result)
    ############ My code End #############

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)