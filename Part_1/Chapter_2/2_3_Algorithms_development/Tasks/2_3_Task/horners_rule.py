import time
def compute_polynomial(x, max_deg, coeffs):
    y = 0
    for i in range(0, max_deg + 1):
        y += coeffs[i] * x ** i
    return y


def horners_polynomial(x, max_deg, coeffs):
    y = 0
    for i in range(max_deg, -1, -1):
        y = coeffs[i] + y * x
    return y


x = 2
max_deg = 0
coeffs = [1] * (max_deg + 1)

tic = time.time()
a = compute_polynomial(x, max_deg, coeffs)
# print(a)
toc = time.time()
print(toc - tic)

tic = time.time()
b = horners_polynomial(x, max_deg, coeffs)
# print(b)
toc = time.time()
print(toc - tic)

print(a == b)
