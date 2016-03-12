print ("What's your name?")
name = input('==>')
print ("How old are you?",end=" ")
age = input()
input("Press enter")
print ("How many tall are you?")
height = input()
print ("How much do you weigh?"),
weight = input()

print ("So, your name is %r, you're %r old, %r tall and %r heavy." % (
    name, age, height, weight))
    
# 1. raw_input() takes input from the user, and always returns a string
