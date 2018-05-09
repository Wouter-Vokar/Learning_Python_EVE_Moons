import csv

# Opens Data.csv to and saves the data in data_intake
# After which each row is saved as an entry in data_input

with open('data.csv', newline='') as data_intake:
    data_intake = csv.reader(data_intake)
    data_input = []

    for row in data_intake:
        data_input.extend(row)

# Splits the long list into separate list entries

split = data_input[0].split('\t')

print("System {}, Planet {}, Moon {}".format(split[0], split[1], split[2]))
