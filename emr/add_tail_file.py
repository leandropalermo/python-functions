def append_last_line(file_path, new_line):
    # Open the file in append mode and add the new line
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(new_line + '\n')

# Example usage
file_path = r'C:\Users\c83838a\Downloads\serasa_places_3_AUG24.txt'
new_line = '0|4314044'  # Replace with the line you want to insert
append_last_line(file_path, new_line)