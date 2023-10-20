from datetime import datetime

cur = datetime.now()
micro = cur.replace(microsecond=0)
print("Without:", micro)
