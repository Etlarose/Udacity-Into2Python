## Please use this space to test and run your code
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
break_num = 0
result = 0


for num in num_list:
    if break_num < 5 and (num % 2) != 0:
        break_num += 1
        #print(break_num)
        result = result + num
        #print(num)
        


print(result)
