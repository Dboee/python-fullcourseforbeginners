lucky_numbers = [4,8,15,16,23,42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends) # Just printing out the list

#friends.extend(lucky_numbers) # Adds lists together

friends.append("Creed") # same as .push() in JS, adds new item to the end
print(friends) 
friends.insert(1, "Kelly") #inserts value wherever you want it 
print(friends) 
print(friends.index("Jim")) 
friends.remove("Kelly") #Removes object from list
print(friends) 
friends.sort()
print(friends) 
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()


friends.pop()
print(friends)
friends.clear() #removes everything
print(friends) 
print(friends2)