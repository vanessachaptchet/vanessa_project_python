import os
import shutil


def organize_files(path):
    if not os.path.exists(path):
        print(f"Path does not exist: {path}")
        return

    folder_map = {
        "csv_files": [".csv"],
        "image_files": [".jpg", ".jpeg", ".png"],
        "text_files": [".txt", ".pdf", ".docx"],
        "excel_files": [".xlsx", ".xls"],
        "code_files": [".py", ".ipynb", ".sql", ".r"],
        "other_files": []
    }

    # Create folders if they do not exist
    for folder_name in folder_map:
        folder_path = os.path.join(path, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    # Organize files
    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)

        # Skip folders
        if not os.path.isfile(file_path):
            continue

        # Do not move important project files
        if file_name in ["organize.py", "README.md"]:
            continue

        _, ext = os.path.splitext(file_name)
        ext = ext.lower()

        moved = False

        for folder_name, extensions in folder_map.items():
            if ext in extensions:
                destination = os.path.join(path, folder_name, file_name)
                if not os.path.exists(destination):
                    shutil.move(file_path, destination)
                    print(f"Moved: {file_name} -> {folder_name}")
                moved = True
                break

        if not moved:
            destination = os.path.join(path, "other_files", file_name)
            if not os.path.exists(destination):
                shutil.move(file_path, destination)
                print(f"Moved: {file_name} -> other_files")


if __name__ == "__main__":
    target_path = "/mnt/c/Users/vanes/Desktop/data_analytics/python"
    organize_files(target_path)