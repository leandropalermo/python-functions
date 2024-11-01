def modify_file(file_path):
    # Read all lines from the file
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Modify the lines
    modified_lines = []
    for i, line in enumerate(lines):
        line = line.rstrip('\n')  # Remove any existing newline characters
        if i == 0 or i == 1:  # First or second line
            modified_lines.append(f"0|{line}")
        elif i == len(lines) - 1:  # Last line
            modified_lines.append(f"0|{line}")
        else:  # All other lines
            modified_lines.append(f"1|{line}")

    # Write the modified lines back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        for modified_line in modified_lines:
            file.write(modified_line + '\n')

# Example usage
file_path = r'C:\Users\c83838a\Downloads\serasa_places_3_AUG24.txt'
modify_file(file_path)
