def modify_content(content):
    """
    Modify the content of the file.
    You can customize this function as needed.
    For now, it converts text to uppercase.
    """
    return content.upper()


def main():
    try:
        # Prompt user for input filename
        input_filename = input("Enter the filename to read: ")

        # Try opening and reading the file
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify content
        modified_content = modify_content(content)

        # Write modified content to a new file
        output_filename = f"modified_{input_filename}"
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"✅ Modified content written to '{output_filename}'")

    except FileNotFoundError:
        print("❌ Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("❌ Error: Unable to read or write the file. Please check file permissions.")
    except Exception as e:
        print(f"❌ Unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
