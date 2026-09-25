# HOAT DONG 6.1
# GIAI THUA BANG DE QUY

def giai_thua_de_quy(n):
    if n <= 1:
        return 1

    return n * giai_thua_de_quy(n - 1)


def giai_thua_lap(n):
    ket_qua = 1

    for i in range(1, n + 1):
        ket_qua *= i

    return ket_qua


print("Giai thua cua 5:")

print(
    giai_thua_de_quy(5),
    "-",
    giai_thua_lap(5)
)


# HOAT DONG 6.2
# FIBONACCI BANG DE QUY


def fibonacci_de_quy(n):
    if n <= 1:
        return n

    return (
        fibonacci_de_quy(n - 1)
        + fibonacci_de_quy(n - 2)
    )


print("\n10 so Fibonacci dau tien:")

for i in range(10):
    print(fibonacci_de_quy(i), end=" ")

print()


print("\nFibonacci thu 10:")
print(fibonacci_de_quy(10))