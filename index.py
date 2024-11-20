def read_and_modify_file(input_file, output_file):
    """Reads a file, modifies its content, and writes it to a new file.

    Args:
        input_file (str): The name of the input file.
        output_file (str): The name of the output file.
    """

    try:
        with open(input_file, 'r') as file:
            content = file.read()
            # Modify the content here (e.g., reverse the lines)
            modified_content = content[::-1]

            with open(output_file, 'w') as new_file:
                new_file.write(modified_content)
        print(f"File '{output_file}' created successfully.")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except IOError:
        print("An I/O error occurred.")

# Get input file name from the user
input_filename = input("Enter the name of the input file: ")

# Get output file name from the user
output_filename = input("Enter the name of the output file: ")

read_and_modify_file(input_filename, output_filename)