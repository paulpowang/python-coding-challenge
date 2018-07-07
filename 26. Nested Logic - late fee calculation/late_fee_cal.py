actual_date = input().split(" ")
expected_date = input().split(" ")
# day, month, year

'''
#turn str list to int list
#however, this will increase the time complexity
for i in range(3):
    actual_date[i] = int(actual_date[i])
    expected_date[i] = int(expected_date[i])
'''

def total_fine_cal(actual_date, expected_date):
    if actual_date[2]>expected_date[2]:
        return 10000
    elif int(actual_date[2])==int(expected_date[2]) and int(actual_date[1])>int(expected_date[1]):
        return 500 * (int(actual_date[1])-int(expected_date[1]))
    elif int(actual_date[2])==int(expected_date[2]) and int(actual_date[1])==int(expected_date[1]) and int(actual_date[0])>int(expected_date[0]):
        return 15 * (int(actual_date[0])-int(expected_date[0]))
    else:
        return 0

total_fine= total_fine_cal(actual_date, expected_date)
print(total_fine)