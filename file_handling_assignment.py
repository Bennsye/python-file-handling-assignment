# ------------------------------------------------------------
# File: file_handling_assignment.py
# Author: Bernard Syengo
# Description:
#   Demonstrates file handling and exception handling in Python.
#   Part 1: Reads from an input file, modifies the content by adding line numbers,
#           and writes to an output file.
#   Part 2: Asks the user for a filename and gracefully handles file errors.
# ------------------------------------------------------------

def read_and_modify_file(input_file, output_file):
    """
    Reads the content of input_file, adds line numbers,
    and writes the modified content into output_file.
    Handles errors if the input file is missing.
    """

    try:
        # Open the input file in read mode ("r")
        with open(input_file, "r") as file:
            content = file.readlines()  # Read all lines into a list

        # Add line numbers to each line using enumerate
        modified_content = [f"{i+1}: {line}" for i, line in enumerate(content)]

        # Open the output file in write mode ("w") and save modified content
        with open(output_file, "w") as file:
            file.writelines(modified_content)

        print(f"✅ Modified content written to {output_file}")

    except FileNotFoundError:
        # Handles the case when input_file does not exist
        print(f"❌ Error: The file '{input_file}' was not found.")
    except Exception as e:
        # Handles any other unexpected errors
        print(f"⚠️ An unexpected error occurred: {e}")


def error_handling_lab():
    """
    Asks the user for a filename, attempts to open it,
    and handles errors such as missing or unreadable files.
    """

    # Prompt the user to type in the filename
    filename = input("Enter the filename you want to read: ")

    try:
        # Try to open the user-specified file in read mode
        with open(filename, "r") as file:
            print("📄 File Content:")
            print(file.read())  # Print the entire file content to console
    except FileNotFoundError:
        # Error when the file does not exist
        print(f"❌ Error: The file '{filename}' does not exist.")
    except PermissionError:
        # Error when the user doesn’t have permission to read the file
        print(f"❌ Error: You don’t have permission to read '{filename}'.")
    except Exception as e:
        # Handles all other unexpected errors
        print(f"⚠️ An unexpected error occurred: {e}")


# ------------------------------------------------------------
# MAIN PROGRAM EXECUTION
# ------------------------------------------------------------
if __name__ == "__main__":
    # Part 1: Run the File Read & Write Challenge
    read_and_modify_file("input.txt", "output.txt")

    # Part 2: Run the Error Handling Lab
    error_handling_lab()
