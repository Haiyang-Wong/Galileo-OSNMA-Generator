import csv

m = []
mess = []
with open("PRN_2.csv", "r") as file1:
    file = csv.reader(file1)
    mess = list(file)

for row in mess:
    print(row[3])

with open('ModifyNavdata_PRN_2.csv', 'a', newline='') as file1:
    file = csv.writer(file1)
    for row in mess:
        m.append(row[0])
        m.append(row[1])
        m.append(row[2])
        c = int(row[0])
        if c % 30 == 25:
            row[3] = row[3][:11] + '1' + row[3][12:]
        m.append(row[3])
        file.writerow(m)
        m = []
