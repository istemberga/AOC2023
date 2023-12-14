import re

regex = r"\d+"
surrounding_size = 1  # Adjust this value to change the size of the square-like shape

# Read the content of the text file
file_path = r"C:\Users\Aleksandar\Desktop\AOC 2023\Day3\input.txt"  # Replace with the actual path to your text file
with open(file_path, 'r') as file:
    file_content = file.read()

# Add \n to the end of each line
formatted_content = "\n".join(file_content.splitlines())



# Split the formatted_content into rows
rows = formatted_content.strip().split('\n')

# Initialize an empty grid to store the positions and values
grid = []

# Initialize a list to store the found numbers
found_numbers = []

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
        invalid_char_found = False
        for i in range(max(0, row_num - surrounding_size), min(len(grid), row_num + surrounding_size + 1)):
            for j in range(max(0, start_col - surrounding_size), min(len(cell), end_col + surrounding_size + 1)):
                if not (grid[i][j].isdigit() or grid[i][j] == '.'):
                    invalid_char_found = True
                    break
            if invalid_char_found:
                break

        # If no invalid character found, save the number
        if invalid_char_found:
            found_numbers.append(int(match.group()))

# Print the saved numbers
print("Found Numbers:", found_numbers)

# Add up the saved numbers
total_sum = sum(found_numbers)
print("Total Sum of Found Numbers:", total_sum)
