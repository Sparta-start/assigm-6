def trap(a, b, h):
    form = ((a+b)/2)*h
    return form

a = float(input())
b = float(input())
h = float(input())
form = trap(a, b, h)
print('{:.2f}'.format(form))
