# Ask the user to enter a word
word = input("Enter a word: ")

# Determine the length of the word
word_length = len(word)

# Ask the user to enter numbers equal to the length of the word
numbers = []

for i in range(word_length):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Function to compute the average of numbers in the list
def compute_average(num_list):
    total = 0
    for n in num_list:
        total += n
    return total / len(num_list)

# Function to compare the average with the word length
def compare_length_and_average(length, average):
    if length > average:
        return "The length of the word is greater than the average."
    elif length < average:
        return "The length of the word is less than the average."
    else:
        return "The length of the word is equal to the average."

# Call the functions
average = compute_average(numbers)
result = compare_length_and_average(word_length, average)

# Display the results
print(numbers)
print("The length of the word is", word_length)
print("The average of the numbers is", average)
print(result)