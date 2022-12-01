list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1)

list2 = [i ** 2 for i in range(10)]

print(list2)

dict1 = {ID:values for ID,values in zip(list1,list2)}

print(dict1)