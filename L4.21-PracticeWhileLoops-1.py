# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

# write your while loop here
while current < number and current > 0:
    #sanity test print(current)
    # multiply the product so far by the current number
    product = product * (current + 1) 
    current += 1
    # increment current with each iteration until it reaches number



# print the factorial of number
print(product)
