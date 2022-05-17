
import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

choice=random.choice(names)
print(f'{choice} is going to buy the meal today!')
