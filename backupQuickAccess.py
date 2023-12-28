import os
import shutil
from datetime import datetime

def backup_automatic_destinations():
    # Get the current user's home directory
    user_home = os.path.expanduser("~")

    # Specify the source folder path
    automatic_destinations_path = os.path.join(
        user_home, "AppData", "Roaming", "Microsoft", "Windows", "Recent", "AutomaticDestinations"
    )

    # Ensure the source folder exists
    if not os.path.exists(automatic_destinations_path):
        print(f"Error: AutomaticDestinations folder '{automatic_destinations_path}' not found.")
        return

    # Create a destination folder in the user's Documents folder with the current date
    today_date = datetime.now().strftime("%Y-%m-%d")
    destination_folder_name = f"QuickAccessBackup_{today_date}"
    destination_path = os.path.join(user_home, "Documents", destination_folder_name)

    # Ensure the destination folder exists, create if not
    if not os.path.exists(destination_path):
        try:
            os.makedirs(destination_path)
            print(f"Created destination folder: '{destination_path}'")
        except Exception as e:
            print(f"Error creating destination folder: {e}")
            return

    try:
        # Get the list of files in the AutomaticDestinations folder
        files = [f for f in os.listdir(automatic_destinations_path) if os.path.isfile(os.path.join(automatic_destinations_path, f))]

        # Copy each file to the destination folder
        for file in files:
            source_file_path = os.path.join(automatic_destinations_path, file)
            destination_file_path = os.path.join(destination_path, file)
            shutil.copy2(source_file_path, destination_file_path)
            print(f"Copied: '{source_file_path}' to '{destination_file_path}'")

        print("Backup completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    backup_automatic_destinations()

    # Keep the console window open until the user presses Enter
    input("Press Enter to exit.")
