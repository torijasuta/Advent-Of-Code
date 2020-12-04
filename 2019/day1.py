import pandas as pd

input_df = pd.read_csv('day1_input.txt', header=None)
input_df.columns=['input']
input_list = input_df['input'].tolist()


# part 1
fuel_counter = 0
for mass in input_list:
    fuel = (mass // 3) - 2
    fuel_counter += fuel

print(fuel_counter)


# part 2
# fuel for the fuel

fuel_for_fuel_counter = 0
fuel_added = fuel_counter

while fuel_added > 0:
    fuel_added = (fuel_added // 3) - 2
    fuel_for_fuel_counter += fuel_added

print(fuel_for_fuel_counter)
total_fuel = fuel_counter + fuel_for_fuel_counter
print(total_fuel)











fuel_counter = 0
for mass in input_list:
    fuel_needed = (mass // 3) - 2
    fuel_counter += fuel_needed
    while fuel_needed > 5:
        fuel_needed = (fuel_needed // 3) - 2
        fuel_counter += fuel_needed

fuel = 0
for datum in input_list:
    fuel_needed = int(datum) // 3 - 2
    fuel += fuel_needed
    while fuel_needed > 5:
        fuel_needed = int(fuel_needed) // 3 - 2
        fuel += fuel_needed

print('Actual Fuel needed is', fuel)



# PART 1
fuel = 0
for datum in input_list:
    fuel += int(datum) // 3 - 2

print('Fuel needed is', fuel)


# Part 2
fuel = 0
for datum in input_list:
    fuel_needed = int(datum) // 3 - 2
    fuel += fuel_needed
    while fuel_needed > 5:
        fuel_needed = int(fuel_needed) // 3 - 2
        fuel += fuel_needed

print('Actual Fuel needed is', fuel)