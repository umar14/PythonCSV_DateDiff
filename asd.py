from datetime import datetime
import csv

with open('data.csv', 'rb') as f:
    reader = csv.reader(f)
    myList = list(reader)


for date in myList:
	

start_date = myList[1][1]
end_date = myList[1][2]


def __datetime(date_str):
    return datetime.strptime(date_str, ' %Y-%d-%m %H:%M:%S')

start = __datetime(start_date)
end = __datetime(end_date)

delta = end - start
print start_date
print end_date
print delta  
print delta.total_seconds() / 60  