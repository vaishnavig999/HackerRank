#Task
#Given names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. 
# For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for name is not found, print Not found instead.

#Note: Your phone book should be a Dictionary/Map/HashMap data structure. 

entrycount = int(input())
dict1 = {}
for i in range (entrycount):
    name, phone = input().split()
    dict1[name] = phone

while(True):
    try:
        name = input()
    except EOFError:
        break
    if name in dict1:
        print(f"{name}={dict1[name]}")
    else:
        print('Not found')