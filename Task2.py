def print_operation_table(operation, num_rows=6, num_columns=6):
    list = [[operation(x, y) for x in range(1, num_columns + 1)] for y in range(1, num_rows + 1)]
    #print(list)
    for i in list:
        print(*[x for x in i])

print_operation_table(lambda x, y: x * y)