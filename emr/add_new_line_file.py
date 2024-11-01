def insert_first_line(file_path, new_line):
    # Read the existing content of the text file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()

    # Insert the new line at the beginning of the content
    content.insert(0, new_line + '\n')

    # Write the updated content back to the text file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(content)


# Example usage
file_path = r'C:\Users\c83838a\Downloads\serasa_places_AUG24.txt'
new_line = '5577343|20240825|41'  # Replace with the line you want to insert
insert_first_line(file_path, new_line)
