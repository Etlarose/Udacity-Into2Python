scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }
#print("Iterating through keys:")
#for key in scores:
    #print(key)

#print("\nIterating through keys and values:")
#for key, value in scores.items():
    #print("Actor: {}    Role: {}".format(key, value))


passed = [key for key, value in scores.items() if value >= 65]# write your list comprehension here
print(passed)
