height = int(input("Zadaj výšku stromu: "))
print(height)


def print_tree(hght):
    for y in range(hght):
        print("*", end=" ")


for i in range(height + 1):
    print_tree(i)
    print()
