import re
file_path = "your folder here"

totalsum = 0
current_word = ""
current_word_reverse = ""
first_number_word = 0
last_number_word = 0

word_to_number = {    # my dictionary for word numbers
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

word_to_number_inverted = {    # my dictionary for reversed numbers
    'eno': 1,
    'owt': 2,
    'eerht': 3,
    'ruof': 4,
    'evif': 5,
    'xis': 6,
    'neves': 7,
    'thgie': 8,
    'enin': 9
}



with open(file_path, 'r') as file:
    # Read each line until the end of the file
    line_number = 1
    while True:

        line = file.readline()
        if not line:  # If the line is empty, it means we have reached the end of the file
            break

        #initialize my variables for the loops
        line_length = len(line)
        position = 0
        first_number = None
        first_word = None
        last_number = None
        found_word = False
        found_word_reverse = False


        #this is the first loop, checks string from LEFT -> RIGHT

        for char in line:
            if char.isdigit() and first_number is None:
                first_number = char
                break
            elif char.isalpha():
                current_word += char.lower()
                for word in word_to_number:
                    if word in current_word:
                        number = word_to_number[word]
                        print(f"The word is: {word}, and the number is: {number}")
                        found_word = True
                        first_number = number
                        print(first_number)

                        break
            if found_word:
                current_word = ""
                break







        #Second loop, this one does the same but checks the string in reverse
        for char in reversed(line):
            if char.isdigit() and last_number is None:
                last_number = char
                break
            elif char.isalpha():
                current_word_reverse += char.lower()

                for word in word_to_number_inverted:
                    if word in current_word_reverse:
                        numbertwo = word_to_number_inverted[word]
                        print(f"The word is: {word}, and the number is: {numbertwo}")
                        found_word_reverse = True
                        last_number = numbertwo

            if found_word_reverse:
                current_word_reverse = ""
                break



        finalnumber =str(first_number) + str(last_number)



        print(f"Line {line_number}: {line.strip()}" + " Exported number :" + str(finalnumber))
        totalsum += int(finalnumber)
        print(str(totalsum))
        line_number += 1

