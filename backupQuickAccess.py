import os
import shutil

def backup_quick_access(quick_access_path, destination_path):
    # Ensure the QUICK ACCESS folder exists
    if not os.path.exists(quick_access_path):
        print(f"Error: QUICK ACCESS folder '{quick_access_path}' not found.")
        return

    # Ensure the destination folder exists, create if not
    if not os.path.exists(destination_path):
        try:
            os.makedirs(destination_path)
            print(f"Created destination folder: '{destination_path}'")
        except Exception as e:
            print(f"Error creating destination folder: {e}")
            return

    try:
        # Get the list of files in the QUICK ACCESS folder
        files = [f for f in os.listdir(quick_access_path) if os.path.isfile(os.path.join(quick_access_path, f))]

        # Copy each file to the destination folder
        for file in files:
            source_file_path = os.path.join(quick_access_path, file)
            destination_file_path = os.path.join(destination_path, file)
            shutil.copy2(source_file_path, destination_file_path)
            print(f"Copied: '{source_file_path}' to '{destination_file_path}'")

        print("Backup completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace this path with your actual QUICK ACCESS folder path
    QUICK_ACCESS_PATH = "%appdata%\microsoft\windows\recent\automaticdestinations"

    # Prompt the user to input the destination folder
    DESTINATION_PATH = input("Enter the destination folder path: ").strip()

    backup_quick_access(QUICK_ACCESS_PATH, DESTINATION_PATH)
