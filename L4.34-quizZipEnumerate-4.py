data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = []

for i in range(len(data)):
    #print(i, data[i])# sanity check
    x, y, z, = data[i]# unpack tuples
    print(x, y, z)
    
#print(data_transpose)
