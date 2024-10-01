#task 1
import math

def hypotenuse(a: float, b: float) -> float:
    """Calculate the hypotenuse of a right triangle given sides a and b."""
    return math.sqrt(a*2 + b*2)
triangles = [
    (3.0, 4.0),  # Example 1: Triangle with sides 3 and 4
    (5.0, 12.0), # Example 2: Triangle with sides 5 and 12
    (8.0, 15.0)  # Example 3: Triangle with sides 8 and 15
]

for a, b in triangles:
    print(f"The hypotenuse of a triangle with sides {a} and {b} is {hypotenuse(a, b):.2f}")








#task 2
import math

def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """Calculate the distance between two points (x1, y1) and (x2, y2)."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
x1, y1 = map(float, input("Enter the first point: ").split())
x2, y2 = map(float, input("Enter the second point: ").split())
dist = distance(x1, y1, x2, y2)
print(f"Distance between ( {x1:.2f}, {y1:.2f} ) and ( {x2:.2f}, {y2:.2f} ) is {dist:.2f}")



#task 3
def reversed(number: int) -> int:
    """Return the number with its digits reversed."""
    return int(str(number)[::-1])
number = int(input("Enter an integer between 1 and 9999: "))
if 1 <= number <= 9999:
    reversed_number = reversed(number)
    print(f"The reversed number is: {reversed_number}")
else:
    print("The number is out of range. Please enter a number between 1 and 9999.")







#task 4
def is_prime(number: int) -> bool:
    """Check if the given number is a prime number."""
    if number <= 1:
        return False
    if number == 2:
        return True  # 2 is the only even prime number
    if number % 2 == 0:
        return False  # All other even numbers are not prime
    
    # Check divisibility by odd numbers up to the square root of the number
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    
    return True

# Find and print all 4-digit prime numbers
print("4-digit prime numbers are:")
for num in range(1000, 10000):
    if is_prime(num):
        print(num, end=" ")




#task 5
def qualityPoints(average: int) -> int:
    """Return the GPA based on the student's average."""
    if 90 <= average <= 100:
        return 4
    elif 80 <= average < 90:
        return 3
    elif 70 <= average < 80:
        return 2
    elif 60 <= average < 70:
        return 1
    else:
        return 0

while True:
    
    average = int(input("Enter the student's average: "))
    
    gpa = qualityPoints(average)
    print(f"{average} on a 4 point scale is {gpa}")
    cont = input("Do you want to enter another average? (yes/no): ").strip().lower()
    if cont != 'yes':
        break




#task 6
def is_bouncy(number: int) -> bool:
    """Check if a number is bouncy."""
    increasing = decreasing = True
    num_str = str(number)
    for i in range(len(num_str) - 1):
        if num_str[i] < num_str[i + 1]:
            decreasing = False
        elif num_str[i] > num_str[i + 1]:
            increasing = False
        if not increasing and not decreasing:
            return True
            
    return False
bouncy_numbers = []
for num in range(1000, 10000):
    if is_bouncy(num):
        bouncy_numbers.append(num)

print("4-digit bouncy numbers:")
print(bouncy_numbers)
print(f"Total count of 4-digit bouncy numbers: {len(bouncy_numbers)}")




#task7
def number_of_factors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count
    
#task 8
import math

def binom(n, k):
    if k > n or k < 0:
        return 0
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
# Example for number_of_factors
print(number_of_factors(12))  # Output: 6 (factors: 1, 2, 3, 4, 6, 12)

# Example for binom
print(binom(5, 2))  # Output: 10

#task 9
import random

def guess_the_number():
    # Generate a random number between 1 and 1000
    number_to_guess = random.randint(1, 1000)
    print("I have a number between 1 and 1000.")
    print("Can you guess my number?")
    
    while True:
        # Ask the user for their guess
        guess = int(input("Please type your guess: "))

        # Check if the guess is too low, too high, or correct
        if guess < number_to_guess:
            print("Too low. Try again.")
        elif guess > number_to_guess:
            print("Too high. Try again.")
        else:
            print("Excellent! You guessed the number!")
            # Ask the player if they want to play again
            play_again = input("Would you like to play again (y or n)? ").lower()
            if play_again == 'y':
                guess_the_number()  # Start a new game
            else:
                print("Thanks for playing!")
                break  # Exit the game

# Start the game
guess_the_number()



#task  11
def int2binary(n):
    binary_list = []
    
    while n > 0:
        remainder = n % 2
        binary_list.append(str(remainder))
        n = n // 2
    
    # Reverse the list to get the correct binary representation
    binary_list.reverse()
    
    # Join the list to form the binary string
    return ''.join(binary_list)

# Program to print binary equivalents of numbers from 100 to 1000
print(f"{'Number':<10}{'Binary Equivalent':<20}")
print("-" * 30)

for number in range(100, 1001):
    binary_equivalent = int2binary(number)
    print(f"{number:<10}{binary_equivalent:<20}")




#task 12
def root(x, n=2):
    return x / n

# Example usage:
result1 = root(10)       
result2 = root(10, 5)

print("Result with default n=2:", result1) 
print("Result with n=5:", result2)      


#task 13
import math

def round_to_nearest(numbers):
    for x in numbers:
        y = math.floor(x + 0.5)
        print(f"Original: {x}, Rounded: {y}")

# Example usage:
numbers = [2.3, 3.7, 4.5, -1.2, -3.8]
round_to_nearest(numbers)



#task 14
import math

# Function to round to the nearest integer
def roundToInteger(number):
    return math.floor(number + 0.5)

# Function to round to the nearest tenth
def roundToTenths(number):
    return math.floor(number * 10 + 0.5) / 10

# Function to round to the nearest hundredth
def roundToHundredths(number):
    return math.floor(number * 100 + 0.5) / 100

# Function to round to the nearest thousandth
def roundToThousandths(number):
    return math.floor(number * 1000 + 0.5) / 1000

# Main program to process multiple numbers
def main():
    count = int(input("How many numbers do you want to process? "))
    
    for _ in range(count):
        number = float(input("Enter number: "))
        rounded_integer = roundToInteger(number)
        rounded_tenths = roundToTenths(number)
        rounded_hundredths = roundToHundredths(number)
        rounded_thousandths = roundToThousandths(number)

        print(f"{number:.6f} rounded to an integer is {rounded_integer:.6f}")
        print(f"{number:.6f} rounded to the nearest tenth is {rounded_tenths:.6f}")
        print(f"{number:.6f} rounded to the nearest hundredth is {rounded_hundredths:.6f}")
        print(f"{number:.6f} rounded to the nearest thousandth is {rounded_thousandths:.6f}")
        print()

# Run the program
main()