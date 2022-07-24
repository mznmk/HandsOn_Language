import datetime
from array import array

print(datetime.time(5, 45, 2))
print(datetime.date.today())

arr = array("i", [1, 2, 3])
arr.append(4)
print(arr.tolist(), arr[0])
