import random

names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

print(len(names))
random_choice = random.randint(0, num_items - 1)
print(random_choice)