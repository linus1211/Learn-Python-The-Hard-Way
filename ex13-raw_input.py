from sys import argv

script, first_name, last_name = argv

middle_name = input("What is your middle name? ")

print ("Your full name is %s %s %s." % (first_name, middle_name, last_name))
