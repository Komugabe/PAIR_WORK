# Pair A Exercise 1
# Richard Caballero
# Maria Assumpta Komugabe

# #-Multiplication Table --- Many lines of code
# n = 12
# multi_table = [['X'] * (n+1) for p in range(n+1)]
# for i in range(1, n+1):
#     multi_table[i][0] = i
#     for k in range(1, n+1):
#         multi_table[0][k] = k
#         multi_table[i][k] = i*k
# print(*multi_table, sep = "\n")

# Multiplication Table --- Single line of code, second line is to print
# Get rid of n variable
multi_table = [['X'] + list(range(1, 13))] + [a[:0] + [a[0]] + a[0:] for a in [[(j+1)*(i+1) for j in range(12)] for i in range(12)]]

print(*multi_table, sep="\n")


# ---Scratch
# for i in range(1 , 13):
# 	print(i, end="\t")
# print()
# print("----------------------------------------------------\n")
# for j in range(1 , 13):
# 	for k in range(1,13):
# 		print(j*k, end="\n")
# print("\n")
#
# n = 12
# Multi = [['X'] * (n+1) for p in range(n+1)]
# print(Multi)

# multi_table = [['X'] + list(range(1, 13))] + [a[:0] + [a[0]] + a[0:] for a in [[(j+1)*(i+1) for j in range(12)] for i in range(12)]]
#
# print(*multi_table, sep="\n")
# for x in range(len(multi_table)):
#     print(multi_table[x])

# multi_table = [['X'] + list(range(1, 13))]
# print(multi_table)
# for i in range(1, 13):
#     print(* [i*j for j in range(1,13)],sep='\t')



