import csv

def rc(file_name):
    with open(file_name, 'r',encoding="utf-8") as f:
        reader = csv.reader(f)
        #print(reader)
        fieldnames = next(reader)#获取数据的第一列，作为后续要转为字典的键名 生成器，next方法获取
        #print(fieldnames)
        csv_reader = csv.DictReader(f,fieldnames=fieldnames) #self._fieldnames = fieldnames   # list of keys for the dict 以list的形式存放键名
        for row in csv_reader:
            d={}
            for k,v in row.items():
                d[k] = v
    return d