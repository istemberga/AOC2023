import re
import sys

file_path = ""

# Define patterns for green, red, and blue
green_pattern = re.compile(r'(\d+)\s*green')
red_pattern = re.compile(r'(\d+)\s*red')
blue_pattern = re.compile(r'(\d+)\s*blue')

# Limiters
max_red = 12
max_green = 13
max_blue = 14

total_line_numbers = 0

greenmin = None
redmin = None
bluemin = None
totalpow = None



# Read content from the file and process line by line
with open(file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        # Find matches for each pattern in the current line
        print(f"Processing Game {line_number}")
        green_matches = green_pattern.findall(line)
        red_matches = red_pattern.findall(line)
        blue_matches = blue_pattern.findall(line)

        # Convert the matches to integers
        green_numbers = [int(match) for match in green_matches]
        red_numbers = [int(match) for match in red_matches]
        blue_numbers = [int(match) for match in blue_matches]

        # The min amount of cubes i can play the games with etc
        greenmin = max(green_numbers)
        redmin = max(red_numbers)
        bluemin = max(blue_numbers)
        totalpow = greenmin * redmin * bluemin

        # If clause
        if (
                all(number <= max_green for number in green_numbers) and
                all(number <= max_red for number in red_numbers) and
                all(number <= max_blue for number in blue_numbers)
        ):
            print(f"Line: {line.strip()}")
            print(f"Green numbers: {green_numbers}")
            print(f"Red numbers: {red_numbers}")
            print(f"Blue numbers: {blue_numbers}")
            print("All good - within my limit! Valid game!")
            print("\n")

            continue

        else:
            print(f"Line: {line.strip()}")
            print("Error - limits crossed!!!!")
            print("\n")

print(f"Total sum of line numbers: {total_line_numbers}")


