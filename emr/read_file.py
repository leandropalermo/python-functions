def read_lines(file_path, num_first_lines=100, num_last_lines=100, encoding='utf-8'):
    first_lines = []
    last_lines = []
    total_lines = 0

    try:
        with open(file_path, 'r', encoding=encoding) as file:
            # Read all lines
            lines = file.readlines()

            total_lines = len(lines)

            # Get the first and last num_first_lines lines
            first_lines = lines[:num_first_lines]
            last_lines = lines[-num_last_lines:]

    except UnicodeDecodeError as e:
        print(f"UnicodeDecodeError: {e}")
        print("Try using a different encoding.")
        return [], [], 0

    return first_lines, last_lines, total_lines


# Corrected file path
file_path = r'C:\Users\c83838a\Downloads\fr.214.places_serasa_serasa_places_Sep24.txt'  # Use raw string

# Try different encodings if you get an error
encodings = ['utf-8', 'iso-8859-1', 'cp1252']

for enc in encodings:
    print(f"Trying encoding: {enc}")
    first_lines, last_lines, total_lines = read_lines(file_path, encoding=enc)

    if first_lines or last_lines:
        print(f"Total number of lines: {total_lines}")

        print("\nFirst 100 lines:")
        for line in first_lines:
            print(line.strip())

        print("\nLast 100 lines:")
        for line in last_lines:
            print(line.strip())
        break
