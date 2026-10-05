a = {a:a**2 for a in range(10)}


print(a)
print(a.keys())
print(a.values())

print


only keys from the dict---------
for i in a.keys():
    print("keys are :",i)

    #only values from the dict -------------------
for i in a.values():
    print("values are",i)

key and valus access the same time 

for k , v in a.items():
    print("key:",k,"value:",v)


a[10] = 110
print(a)
