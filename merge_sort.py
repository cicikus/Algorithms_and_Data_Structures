import random

def merge_sort(A, p, r):
	# A: an array
	# p, r: starting and ending indices of a subarray of A
	# result: The elements of the sub array A[p...r]
	# are sorted into non-decreasing order.
	if p >= r:
		# then already sorted: do nothing
		return A
	else:
		q = int((p+r)/2)
		print("Calling merge_sort(A, ", p, ", ", q, ") on ", A[p:q+1], sep='')
		merge_sort(A, p, q)
		print("Calling merge_sort(A, ", q+1, ", ", r, ") on ", A[q+1:r+1], sep='')
		merge_sort(A, q+1, r)
		print("Calling merge(A, ", p, ", ", q, ", ", r, ") on ", A[p:q+1], " and ", A[q+1:r+1], sep='')
		merge(A, p, q, r)

def merge(A, p, q, r):
	# A: an array
	# p, q, r: indices into A. Each of subarrays A[p...q] and A[q+1...e] is assumed
	# to be already sorted.
	# Result: The subarray A[p...r] contains the elements originally in A[p...q] and
	# A[q+1...r], but now the entire subarray A[p...r] is sorted.
	n1 = q-p+1
	n2 = r-q
	B = A[p:q+1]
	C = A[q+1:r+1]
	B.append(float("inf"))
	C.append(float("inf"))
	i = 0
	j = 0
	for k in range(p, r+1):
		if B[i] <= C[j]:
			A[k] = B[i]
			i += 1
		else:
			A[k] = C[j]
			j += 1


list10 = []
for i in range(10):
	list10.append(random.randrange(1, 100))

print(list10)
merge_sort(list10, 0, len(list10)-1)
print(list10)
