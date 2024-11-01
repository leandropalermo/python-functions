def insert_before_second_to_last_line(filename, new_line):
    """
    Inserts a new line before the second-to-last line in the specified file.

    :param filename: The path to the file to modify.
    :param new_line: The new line of text to insert.
    """
    try:
        # Read the entire file into a list of lines
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Check if there are at least two lines
        if len(lines) < 2:
            raise ValueError("The file must have at least two lines.")

        # Insert the new line before the second-to-last line
        second_to_last_index = -2
        lines.insert(second_to_last_index, new_line + '\n')

        # Write the updated lines back to the file
        with open(filename, 'w', encoding='utf-8') as file:
            file.writelines(lines)

        print(f"Successfully inserted the new line before the second-to-last line in {filename}.")

    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
filename = r'C:\Users\c83838a\Downloads\serasa_places_3_AUG24.txt'
new_line = '1|70661026000166|377797783|RESTAURANTE TRES MOUR|RESTAURANTE TRES MOUR|ROD 452 KM 261 1|RODOVIA BR-452|PERDIZES|PERDIZES|MG|MG|38170-000|38170-000|BRA|BRA|||5812|||EAP|ACF|2012-04-11 00:00:00|N|Y|Y|Y|Y|Y|Y|-19.352410|-47.286233|STREET|b|N|N|Y|5812|NON-AGGREGATED EATING PLACES  RESTAURANTS 5812|5812|10001460|NON-AGGREGATED|131|229|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|1|0|0|0|0|0|0|0|0|0'
insert_before_second_to_last_line(filename, new_line)