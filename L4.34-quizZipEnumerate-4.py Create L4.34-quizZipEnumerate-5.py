cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]
# write your for loop here

for i, c in enumerate(cast): #separate the index from the value
    #print(i, c + " " + str(heights[i])) #sanity check to see if the index separated from value
    cast[i] = c + " " + str(heights[i]) #add the value from the heights to the cast based on the index number
    



print(cast)
