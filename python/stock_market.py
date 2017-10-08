import csv

data = {}

# with open('stocks-us-adjClose.csv', rb) as f:
#     imported_data = csv.reader(f)
#     for row in imported_data:
#         print(row)


reader = csv.DictReader(open('stocks-us-adjClose.csv'))

for row in reader:
    print(row)


 # open('stocks-us-adjClose.csv', newline="")
 #    csv.reader(data)