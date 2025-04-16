import os

def modify_content(text):
    # Example modification: Convert to uppercase
    return text.upper()

def read_and_write_file():
    input_filename = input("Enter the name of the file to read: ")

    try:
        # Check if the file exists
        if not os.path.exists(input_filename):
            raise FileNotFoundError(f"The file '{input_filename}' does not exist.")

        # Open the input file with UTF-8 encoding
        with open(input_filename, 'r', encoding='utf-8') as infile:
            content = infile.read()
            print("✅ File read successfully.")
        
        # Modify the content
        modified_content = modify_content(content)

        # Generate output filename in the same directory as the input file
        base_name = os.path.basename(input_filename)
        output_filename = "modified_" + base_name

        # Write the modified content to the output file
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.write(modified_content)
            print(f"✅ Modified content written to: {output_filename}")

    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
    except PermissionError:
        print("❌ Error: Permission denied when accessing the file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    read_and_write_file()