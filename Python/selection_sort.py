import random

def linear_search(A, n, i, x):
	# A: array, n: number of elements in the array, i: index,
	# x: number that is searched in the array
	if i > n:
		return -1
	elif i <= n and A[i] == x:
		return i
	elif i <= n and A[i] != x:
		return linear_search(A, n, i + 1, x)

def find_smallest(A, n, i):
	smallest_index = i
	for j in range(i, n):
		if A[j] < A[smallest_index]:
			smallest_index = j
	return smallest_index

def selection_sort(A, n):
	for i in range(0, n):
		print(A)
		smallest_index = find_smallest(A, n, i)
		temp = A[smallest_index] 
		A[smallest_index] = A[i]
		A[i] = temp
	return A


list10 = []
for i in range(10):
	list10.append(random.randrange(1, 100))

print(list10)
index_smallest = find_smallest(list10, len(list10), 0)
print("list10[", index_smallest, "] = ", list10[index_smallest], sep='')
selection_sort(list10, len(list10))
print("\nThe last print\n")
print(list10)