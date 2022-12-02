# Open the input file and read its contents into a string
with open('input.txt', 'r') as f:
    input_str = f.read()

# Split the input string into a list of strings
input_list = input_str.strip().split('\n')

# Initialize the list of top three Elves and their total Calories
top_three = [(0, 0), (0, 0), (0, 0)]

# Initialize the current Elf's total Calories
current_elf_calories = 0

# Loop through each item in the input list
for item in input_list:
    # If the item is a blank line, check if the current Elf's total Calories
    # is greater than any of the Elves in the top three, and if so, update
    # the list of top three Elves accordingly
    if item == '':
        if current_elf_calories > top_three[0][1]:
            top_three[2] = top_three[1]
            top_three[1] = top_three[0]
            top_three[0] = (current_elf_calories, current_elf_calories)
        elif current_elf_calories > top_three[1][1]:
            top_three[2] = top_three[1]
            top_three[1] = (current_elf_calories, current_elf_calories)
        elif current_elf_calories > top_three[2][1]:
            top_three[2] = (current_elf_calories, current_elf_calories)

        # Reset the current Elf's total Calories and continue to the next item
        current_elf_calories = 0
        continue

    # Otherwise, the item is a food item, so add its Calories to the
    # current Elf's total Calories
    current_elf_calories += int(item)

# Compute the total number of Calories carried by the top three Elves
total_calories = sum([t[1] for t in top_three])

# Print the total number of Calories carried by the top three Elves
print(total_calories)
