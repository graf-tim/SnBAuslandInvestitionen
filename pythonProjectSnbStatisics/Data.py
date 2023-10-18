import csv


class Data:
    def __init__(self, row):
        self.direktinvestitionen = row[1]
        self.portfolioinvestitionen = row[2]
        self.derivate = row[3]
        self.uebrigeinvestitionen = row[4]
        self.waehrungsreserven = row[5]
        self.nettoauslandvermoegen = row[6]


class Main:
    # Read data out of csv
    file = open("data.csv", "r")
    data = list(csv.reader(file, delimiter=";"))
    file.close()
    print(data)
    # Format Data in to Data Class
    dataList = {}
    type(dataList)
    for x in data:
        dataList[x[0]] = Data(x)
    # print to check if data is formatted right
    for key in dataList:
        print(key, "=>", dataList[key].direktinvestitionen)
