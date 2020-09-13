# Python 3 implementation of the approach 

# Function to find all unique combination of 
# given elements such that their sum is K 
def unique_combination(l, sum, K, local, A): 
	
	# If a unique combination is found 
	if (sum == K): 
		print("{", end = "") 
		for i in range(len(local)): 
			if (i != 0): 
				print(" ", end ="") 
			print(local[i], end = "") 
			if (i != len(local) - 1): 
				print(", ", end = "") 
		print("}") 
		return

	# For all other combinations 
	for i in range(l, len(A), 1): 
		
		# Check if the sum exceeds K 
		if (sum + A[i] > K): 
			continue

		# Check if it is repeated or not 
		if (i == 1 and
			A[i] == A[i - 1] and i > l): 
			continue

		# Take the element into the combination 
		local.append(A[i]) 

		# Recursive call 
		unique_combination(i + 1, sum + A[i], 
								K, local, A) 

		# Remove element from the combination 
		local.remove(local[len(local) - 1]) 

# Function to find all combination 
# of the given elements 
def Combination(A, K): 
	
	# Sort the given elements 
	A.sort(reverse = False) 

	local = [] 

	unique_combination(0, 0, K, local, A) 

# Driver code 
if __name__ == '__main__': 
	A = [2, 3, 4, 22, 1, 44, 5] 

	K = 11

	# Function call 
	Combination(A, K) 
	
# This code is contributed by 
# Surendra_Gangwar 
