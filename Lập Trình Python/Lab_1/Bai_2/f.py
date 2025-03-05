def print_hollow_triangle(n):
    for i in range(n):
        for j in range(i + 1):
            if j == 0 or j == i or i == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
n = int(input("Nhập số hàng: "))
print_hollow_triangle(n)
    