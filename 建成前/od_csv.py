import csv


with open('od.csv', "r") as f:
    reader = list(csv.reader(f))
    od = []
    for i in range(len(reader)-1):
        for j in range(len(reader[i+1])-1):
            odi2j = [int(reader[0][j+1]), int(reader[i+1][0]), int(reader[i+1][j+1])]
            od.append(odi2j)

csvFile=open("test.csv",'w',newline='')
try:
    writer=csv.writer(csvFile)
    for i in range(len(od)):
        writer.writerow(od[i])
finally:
    csvFile.close()

