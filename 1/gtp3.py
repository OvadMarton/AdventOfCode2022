# Open the input file in read-only mode
with open('input.txt', 'r') as input_file:
    # Read the entire contents of the file as a string
    input_str = input_file.read()

# Split the input string into a list of strings
input_list = input_str.strip().split('\n')

# Initialize the maximum number of Calories seen so far
max_calories = 0

# Initialize the current Elf's total Calories
current_elf_calories = 0

# Loop through each item in the input list
for item in input_list:
    # If the item is a blank line, reset the current Elf's total Calories
    # and continue to the next item
    if item == '':
        current_elf_calories = 0
        continue

    # Otherwise, the item is a food item, so add its Calories to the
    # current Elf's total Calories
    current_elf_calories += int(item)

    # Update the maximum number of Calories seen so far, if needed
    max_calories = max(max_calories, current_elf_calories)

# Print the total number of Calories carried by the Elf carrying the most Calories
print(max_calories)
