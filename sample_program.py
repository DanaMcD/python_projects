# Say hello
print "Hi there. I'm a Python program!"

# Run a loop
print "Let's count to 10!"
for i in range(0, 10):
    print i

# List off some pairs
relationships_dict = {
    'Sonny': 'Cher', 
    'Madonna': 'Guy Ritchie', 
    'Adam': 'Eve' 
}

print "Let's list off some famous couples with a loop through a dict..."

for x, y in relationships_dict.items():
    print x + ": " + y

# End the program
print "That's all this sample program does. Exiting now ... goodbye!"

