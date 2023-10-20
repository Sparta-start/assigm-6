from datetime import datetime, timedelta

cur = datetime.now()
yest = cur - timedelta(days=1)
tom = cur + timedelta(days=1)

print("Yesterday:", yest)
print("Today:", cur)
print("Tomorrow:", tom)