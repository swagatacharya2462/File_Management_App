import os

def create_file(fileName):
    """Create a new file with the specified name."""
    try:
        with open(fileName, 'x') as f:
            print(f"File '{fileName}' created successfully!")
    except FileExistsError:
        print(f"File '{fileName}' already exists!")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_all_files():
    """Display all files in the current directory."""
    files = os.listdir()
    if not files:
        print("No files found.")
    else:
        print("Files in directory:")
        for file in files:
            print(file)

def delete_file(fileName):
    """Delete the specified file."""
    try:
        os.remove(fileName)
        print(f"'{fileName}' has been deleted successfully!")
    except FileNotFoundError:
        print(f"File '{fileName}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_file(fileName):
    """Read and display the content of the specified file."""
    try:
        with open(fileName, "r") as f:
            content = f.read()
            print(f"Content of '{fileName}':\n{content}")
    except FileNotFoundError:
        print(f"File '{fileName}' doesn't exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def edit_file(fileName):
    """Append content to the specified file."""
    try:
        with open(fileName, "a") as f:
            content = input("Enter data to add: ")
            f.write(content + "\n")
            print(f"Content added to '{fileName}' successfully!")
    except FileNotFoundError:
        print(f"File '{fileName}' doesn't exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """Main function to run the file management app."""
    while True:
        print("\nFILE MANAGEMENT APP")
        print("1: Create file")
        print("2: View all files")
        print("3: Delete file")
        print("4: Read file")
        print("5: Edit file")
        print("6: Exit")

        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            fileName = input("Enter the file name to create: ")
            create_file(fileName)
        elif choice == "2":
            view_all_files()
        elif choice == "3":
            fileName = input("Enter the name of the file you want to delete: ")
            delete_file(fileName)
        elif choice == "4":
            fileName = input("Enter file name to read: ")
            read_file(fileName)
        elif choice == "5":
            fileName = input("Enter file name to edit: ")
            edit_file(fileName)
        elif choice == "6":
            print("Closing the app...")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
