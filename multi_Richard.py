

# #-Multiplication Table
# n = 12
# Multi = [['X'] * (n+1) for p in range(n+1)]
# for i in range(1, n+1):
#     Multi[i][0] = i
#     for k in range(1, n+1):
#         Multi[0][k] = k
#         Multi[i][k] = i*k
# print(*Multi, sep = "\n")



# ---From Maria
# print("\t\t\tMULTIPLICATION TABLE\n")
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

# print(*multi_table, sep="\n")

number = 13

for i in range(1, 13): 
    print(* [i*j for j in range(1,13)],sep='\t')
    
