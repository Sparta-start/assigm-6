def even_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield str(i)
n = int(input("N: "))
even = even_generator(n)
result = ','.join(even)
print(result)