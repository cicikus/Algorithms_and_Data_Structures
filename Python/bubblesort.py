import random

def bubblesort(A):
	for i in range(len(A)-2):
		for j in range(len(A)-1, i, -1):
			if A[j] < A[j-1]:
				temp = A[j]
				A[j] = A[j-1]
				A[j-1] = temp
			print(A)
	#return A

list10 = []
for i in range(10):
	list10.append(random.randrange(1, 100))

print(list10)
bubblesort(list10)
print("\nThe last print\n")
print(list10)

# for i in range(len(list10), 0, -1):
# 	print(i)