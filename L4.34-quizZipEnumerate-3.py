cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

#define names and heights here
names = []
heights = []

for i in range(len(cast)):
    names, heights = zip(*cast)


print(names)
print(heights)
