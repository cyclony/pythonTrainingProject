#read csv via csv module
import csv
import collections
with open('area.csv',mode='r') as f:
    csv_file = csv.reader(f)
    headings = next(csv_file)
    Area = collections.namedtuple('Area', headings)
    for row in csv_file:
        area = Area(*row) #将row列表或者元组中每个数据展开后放入参数表中
        print(area.AREA_CODE)



