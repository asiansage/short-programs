# Wildfire StarBreak DPS calculator
# Calculates the average damage output of a Wildfire shell in StarBreak, based on a few parameters
import decimal
import random

lowest_damage = int(input('What is the lowest damage your weapon can do? \n'))
highest_damage = int(input('What is the highest damage your weapon can do? \n'))
shots = int(input('How many shots does your weapon output? \n'))
pen = input("Answer with 'y' or 'n': Does your weapon have penetrating+explosive ammo? \n")
if (pen == 'y'):
    shots *= 2
weapon_type = input("Answer with 'y' or 'n': Is your weapon a repeater? \n")
if (weapon_type == 'y'):
    fire_rate = 10
else:
    fire_rate = int(input('What is the recorded speed on the weapon? \n')) * 0.02
crit_rate = int(input("What is your crit rate (rounded)? \n"))
crit_dmg = float(input("What is your crit multiplier (as written)? \n"))
dmg_mult = ((float(input("What is your damage multiplier %? \n")))/100)+1

cycles = 100
total_dmg = 0
while (cycles != 0):
    if random.randint(1, 100) <= crit_rate:
        total_dmg += (random.randint(lowest_damage, highest_damage) * crit_dmg) * fire_rate * shots *dmg_mult
    else:
        total_dmg += random.randint(lowest_damage, highest_damage) * fire_rate * shots *dmg_mult
    cycles -= 1
print('Your damage per second is: ', total_dmg / 100)
