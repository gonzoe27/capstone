name = input ("What is your name?: ")

print ("Hello " + name + "!")

letters = len(name) # how many letters are in the name
print (f"Your name has {letters} letters in it.")

birthday_month = input ("What month were you born in?: ") 

if birthday_month.lower() == "August":
    print ("Happy birthday month!")
else:
    print ("This month is not your birthday month.")