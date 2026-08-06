person = "Aman"
coins = 3

#############
#  concatenation strings 
print( "\n"+ person + " has " + str(coins) + " coins left." )

#############
#previous %s formatting

print("\n%s has %s coins left." %(person,coins))

#using string.format() function
message =("\n{} has {} coins left." .format(person,coins))
print(message)


player = {'person': 'Dave' , 'coins':3}
message =("\n{person} has {coins} coins left." .format(**player))
print(message)


#########
#using f-string
message = f"\n {person} has {coins} coins left."
print(message)

message = f"\n {person} has {10} coins left."
print(message)

##########
# we can passs formatting options

num = 10
print(f"\n 2.25 times {num} is {2.25 * num:2f}")