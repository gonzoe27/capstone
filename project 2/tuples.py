#Tuples

cats = ('leopard' , 'tiger' , 'cheetah') #often use ()
birds = 'cardinal' , 'robin' , 'swan' #but you don't have to use them 

print(cats[0]) #index tuples like lists 
print(cats[1:3]) #slice tuples like lists 

#can't add or modify to tuples once they are created 

for birds in birds:
    print(birds)
# you can loop over tuples like lists

#the can be useful for returning multiple values from a function
def get_random_cat_and_pattern():
    return 'leopard' , 'spots' # return a tuple 

#unpack your tuple to conveniently get both values in a separate variable
cat, pattern = get_random_cat_and_pattern()


#more examples 

city_state = [ ('Seattle', 'WA'), ('Portland', 'OR') , ('San Francisco', 'CA') ]
print(len(city_state))

first_city_state = city_state[0]
print(first_city_state)

print(first_city_state[0])
print(first_city_state[1]) # doesn't jump to portland rather goes to the state 

city, state = first_city_state
print(city)
