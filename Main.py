import csv

# Opens Data.csv to and saves the data in data_intake
# After which each row is saved as an entry in data_input

with open('data.csv', newline='') as data_intake:
    data_intake = csv.reader(data_intake)
    data_input = []

    for row in data_intake:
        data_input.extend(row)


def ore_price_check(moon_number):

    ore_id = []
    ore_fraction = []

    split_data_input = data_input[moon_number].split('\t')

    i = 3

    while i < (len(split_data_input)):

        print(split_data_input[i])
        print(split_data_input[i+1])
        i = i + 6

    return ore_id, ore_fraction


for moon_numbers in range(len(data_input)):

    ore_price_check(moon_numbers)
