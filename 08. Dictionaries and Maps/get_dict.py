#get size
size = input()


#create empty dictionary
dict = {}

counter = 1
#update dictionary
while counter <= int(size):
    key, value = input().split(' ')
    dict.update({key:value})
    counter = counter + 1

#get the following input
#check the dictionary
#print the result

x = input()
while x !='':
    
    if x in dict:
        print(x + '='+dict.get(x))
    else:
        print('Not found')
    try:
        x = input()
    except Exception:
        break
