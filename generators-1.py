def squareEqual(N):
    for i in range(N):
        yield i**2

N = int(input())
for square in squareEqual(N):
    print(square)
