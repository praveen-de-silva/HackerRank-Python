# ================================
# PROGRAM : Set .unoin() Operation
# ================================

n = int(input())
set1 = set(map(int, input().split()))
b = int(input())
set2 = set(map(int, input().split()))

allStudents = set1.union(set2) # students of at least one course

print(len(allStudents))