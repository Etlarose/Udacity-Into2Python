# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here
#while len(news_ticker) <= 140:
index = 0
letter_count = 0
while index < len(headlines):
    letters = headlines[index]
    #print(letters)
    index = index + 1
    print(index)
    for letter in letters:
        if letter_count <= 140:
            #print(letter)
            news_ticker = news_ticker + letter
            letter_count = letter_count + 1
            #print(letter_count)
        else:
            break


#for index in range(len(headlines)):
    #print(index)
    #if len(news_ticker) <= 140:
        #news_ticker = news_ticker + " " + index
    #else:
        #break


print(news_ticker)
