limit = 50
nearest_square = 0
x = 1
break_num = 0
# write your while loop here
while break_num < limit:
    break_num = x * x
    if break_num > limit:
        #print(nearest_square)
        break
    # print(nearest_square)
    else:
        nearest_square = x * x
        x += 1
        #print(x)

print(nearest_square)
