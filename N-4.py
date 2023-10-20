from datetime import datetime

first = int(input())
second = datetime(2023, 10, 15, 14, 30, 0)

raznica = (second - first).total_seconds()
print("Time Difference in Seconds:", raznica)
