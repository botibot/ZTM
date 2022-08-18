#Lists
basket = [1,2,3,4,5]


#adding
basket.append(100)
basket.insert(4, 400)
basket.extend([200, 201])

#removing
basket.pop() #can remove items by index
basket.remove(4) #removes a value
#basket.clear() #removes everything on the list

#looking for a value in a list
print(1 in basket)
print(basket.count(1))

#printing
print(basket)
print(len(basket))

print(sorted(basket)) # creates a new list not altering the original
print(basket)
basket.sort() #sorts the original list
print(basket)

#reverses the list same as basket.reverse()
print(basket[::-1])

#makes a copy of the list
print(basket[:])

print(list(range(100)))
print(list(range(1,101)))

new_sentence = ' '.join(['hi', 'my', 'name', 'is', 'what?'])
print(new_sentence)

#list unpacking
basket = [1,2,3,4,5,6,7,8,9]
a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
print(a,b,c,d)
print(other)

#None
weapons = None