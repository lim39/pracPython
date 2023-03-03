li = [1, 3, 5, 5, 7, 7, 8]


#li=set(li)

#print(li)
remove_set = {3, 5}

li = [i for i in li if i not in remove_set]
print(li)