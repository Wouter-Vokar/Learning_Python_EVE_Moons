import csv

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    w = []
    for row in reader:
        w.extend(row)

print(w[5])
