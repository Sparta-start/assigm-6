from datetime import datetime, timedelta

cur = datetime.now()
five = cur - timedelta(days=5)

print("Now:", cur)
print("5 days ago", five)
