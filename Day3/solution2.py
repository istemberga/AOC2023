import re

regex = r"\d+"
surrounding_size = 1  # Adjust this value to change the size of the square-like shape

# Read the content of the text file
file_path = r"your file path here"  # Replace with the actual path to your text file
with open(file_path, 'r') as file:
    file_content = file.read()

# Add \n to the end of each line
formatted_content = "\n".join(file_content.splitlines())

# Split the formatted_content into rows
rows = formatted_content.strip().split('\n')

# Initialize an empty grid to store the positions and values
grid = []

# Initialize a dictionary to store the found numbers with their coordinates
found_numbers = {}

# Save the position of the first asterisk
asterisk_position = None

# Loop through each row and convert it into a list of characters
for row_num, row in enumerate(rows):
    grid_row = list(row)
    grid.append(grid_row)

# Use the regular expression to find matches in the grid
for row_num, row in enumerate(grid):
    col_num = 0
    cell = "".join(row)
    cell_matches = re.finditer(regex, cell)
    for match in cell_matches:
        start_col = col_num + match.start()
        end_col = col_num + match.end() - 1

        # Check the characters in the surrounding square
        asterisk_found = False
        for i in range(max(0, row_num - surrounding_size), min(len(grid), row_num + surrounding_size + 1)):
            for j in range(max(0, start_col - surrounding_size), min(len(cell), end_col + surrounding_size + 1)):
                if grid[i][j] == '*':
                    asterisk_found = True
                    asterisk_position = (i, j)
                    break
            if asterisk_found:
                break

        # If an asterisk is found, check if the number shares the same coordinates
        if asterisk_found:
            current_coordinates = asterisk_position
            current_number = int(match.group())

            # Check if the coordinates have been seen before
            if current_coordinates in found_numbers:
                found_numbers[current_coordinates].append(current_number)
            else:
                found_numbers[current_coordinates] = [current_number]

# Calculate the product of numbers associated with the same coordinates
product_sum = 0
for coordinates, numbers in found_numbers.items():
    if len(numbers) > 1:
        product = 1
        for number in numbers:
            product *= number
        product_sum += product
        print(f"Coordinates: {coordinates}, Numbers: {numbers}, Multiplied: {product}")

# Print the sum of all multiplied numbers
print("Sum of multiplied numbers:", product_sum)
