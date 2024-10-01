#task 1
# Input a line of text from the user
text = input("Enter a line of text:\n")

# Convert the text to uppercase and lowercase
uppercase_text = text.upper()
lowercase_text = text.lower()

# Output the results
print("The line in uppercase is:")
print(uppercase_text)

print("The line in lowercase is:")
print(lowercase_text)









#task2 
# Input a string from the user
text = input("Enter a string:\n")

# Count the number of spaces in the string
space_count = text.count(' ')

# Estimate the number of words
# We add 1 because the number of words is typically one more than the number of spaces
word_estimate = space_count + 1

# Output the estimate
print("The estimated number of words is:", word_estimate)



#task 3
# Input a string from the user
s = input("Enter a string:\n")

# Convert the string to lowercase
s = s.lower()

# Remove all periods and commas
s = s.replace('.', '').replace(',', '')

# Print the resulting string
print("The resulting string is:")
print(s)




#task 4
# Initial list
ids = [4353, 2314, 2956, 3382, 9362, 3900]

# 1. Remove 3382 from the list
ids.remove(3382)

# 2. Get the index of 9362
index_9362 = ids.index(9362)
print("The index of 9362 is:", index_9362)

# 3. Insert 4499 in the list after 9362
ids.insert(index_9362 + 1, 4499)

# 4. Extend the list by adding [5566, 1830] to it
ids.extend([5566, 1830])

# 5. Reverse the list
ids.reverse()

# 6. Sort the list
ids.sort()

# Print the final list
print("The final sorted list is:", ids)



#task 5
import random

# Number of simulations
num_simulations = 10000

# Initialize a dictionary to count occurrences of each possible roll (2 to 12)
roll_counts = {total: 0 for total in range(2, 13)}

# Simulate rolling two dice 10,000 times
for _ in range(num_simulations):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    roll_total = die1 + die2
    roll_counts[roll_total] += 1

# Print the results in a table format
print("Roll Total | Percentage")
print("------------------------")
for total in range(2, 13):
    percentage = (roll_counts[total] / num_simulations) * 100
    print(f"{total:^10} | {percentage:.2f}%")





#task 6
from collections import Counter

def mean(numbers):
    """Calculate the mean of a list of numbers."""
    if not numbers:
        return 0  # Return 0 if the list is empty
    return int(sum(numbers) // len(numbers))

def median(numbers):
    """Calculate the median of a list of numbers."""
    if not numbers:
        return 0  # Return 0 if the list is empty
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        # For even length, return the average of the two middle numbers
        return int((sorted_numbers[mid - 1] + sorted_numbers[mid]) // 2)
    else:
        # For odd length, return the middle number
        return sorted_numbers[mid]

def mode(numbers):
    """Calculate the mode of a list of numbers."""
    if not numbers:
        return 0  # Return 0 if the list is empty
    count = Counter(numbers)
    max_count = max(count.values())
    mode_values = [num for num, freq in count.items() if freq == max_count]
    return int(min(mode_values))  # Return the smallest mode if there are multiple

# Example usage
numbers = [1, 2, 2, 3, 4, 5, 5, 5]

print("Mean:", mean(numbers))
print("Median:", median(numbers))
print("Mode:", mode(numbers))





#task 7
def rotate_list(lst):
    """Rotate the elements of the list."""
    if len(lst) == 0:
        return lst  # Return an empty list if the input list is empty
    return lst[1:] + [lst[0]]

# Example usage
original_list = [1, 2, 3, 4, 5]
rotated_list = rotate_list(original_list)

print("Original list:", original_list)
print("Rotated list:", rotated_list)





import random

def generate_random_list(size):
    """Generate a list of random 0s and 1s."""
    return [random.randint(0, 1) for _ in range(size)]

def longest_run_of_zeros(lst):
    """Find the longest run of consecutive zeros in the list."""
    max_run = 0
    current_run = 0


    for number in lst:
        if number == 0:
            current_run += 1
            if current_run > max_run:
                max_run = current_run
        else:
            current_run = 0

    return max_run

# Generate a list of 100 random integers (0 or 1)
random_list = generate_random_list(100)

# Find the longest run of zeros
longest_run = longest_run_of_zeros(random_list)

# Print the results
print("Random list:", random_list)
print("Longest run of zeros:", longest_run)


#task 9
import numpy as np

# Function to read matrix size and data from the user
def read_matrix():
    # Read matrix dimensions
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    # Initialize an empty matrix
    matrix = []
    
    # Read matrix elements from the user
    print("Enter the matrix elements row by row:")
    for i in range(rows):
        row = list(map(float, input().split()))
        matrix.append(row)
    
    return np.array(matrix)

# Function to print matrix
def print_matrix(matrix, name):
    print(f"\n{name} Matrix:")
    for row in matrix:
        print(" ".join(map(str, row)))

# Main function
def main():
    # Read matrix from user
    matrix = read_matrix()
    
    # Compute transpose
    transpose = np.transpose(matrix)
    
    # Compute matrix product (matrix * matrix)
    try:
        product = np.matmul(matrix, matrix)
    except ValueError:
        product = "Matrix multiplication not possible with the given dimensions."

    # Print matrices
    print_matrix(matrix, "Original")
    print_matrix(transpose, "Transpose")
    if isinstance(product, str):
        print(product)
    else:
        print_matrix(product, "Product")

# Run the main function
if __name__ == "__main__":
    main()