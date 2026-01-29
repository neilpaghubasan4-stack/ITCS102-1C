word = input("Enter a word: ")

word_length = len(word)

numbers = []

for i in range(word_length):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

def compute_average(num_list):
    total = 0
    for n in num_list:
        total += n
    return total / len(num_list)

def compare_length_and_average(length, average):
    if length > average:
        return "The length of the word is greater than the average."
    elif length < average:
        return "The length of the word is less than the average."
    else:
        return "The length of the word is equal to the average."

average = compute_average(numbers)
result = compare_length_and_average(word_length, average)

print(numbers)
print("The length of the word is", word_length)
print("The average of the numbers is", average)
print(result)