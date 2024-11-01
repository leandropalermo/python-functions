def delete_last_line(filename):
    """
    Deletes the last line from the specified file.

    :param filename: The path to the file from which to delete the last line.
    """
    try:
        # Read the entire file into a list of lines
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Check if there is at least one line to remove
        if not lines:
            raise ValueError("The file is empty. No lines to remove.")

        # Remove the last line
        lines.pop()

        # Write the updated lines back to the file
        with open(filename, 'w', encoding='utf-8') as file:
            file.writelines(lines)

        print(f"Successfully deleted the last line from {filename}.")

    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
filename = r'C:\Users\c83838a\Downloads\serasa_places_3_AUG24.txt'
delete_last_line(filename)
