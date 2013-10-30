from collections import Counter

A = [0,0,1,0,0,0,0,0,0,1,0,1,1,0,1,0,0,0,0,0]
A = sorted(A)

for i in A:
	A[i] = float(A[i])

def solve_mean(input_array):
	return sum(input_array) / len(input_array)
	
def solve_median(input_array):
	half_index = len(input_array)/2
	if len(input_array)%2 == 0:
		return (input_array[half_index] + input_array[half_index+1])/2.0
	else:
		return input_array[half_index]

def solve_mode(input_array):
	data = Counter(input_array)
	mode = data.most_common(1)
	print mode
# print solve_mean(A)
# print solve_median(A)
print solve_mode(A)