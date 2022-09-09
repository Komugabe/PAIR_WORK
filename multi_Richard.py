

#-Multiplication Table
n = 12
Multi = [['X'] * (n+1) for p in range(n+1)]
for i in range(1, n+1):
    Multi[i][0] = i
    for k in range(1, n+1):
        Multi[0][k] = k
        Multi[i][k] = i*k
print(*Multi, sep = "\n")


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



