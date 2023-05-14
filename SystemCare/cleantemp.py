import os
import tempfile
import shutil


class TempCleaner:
    def __init__(self):
        self.temp_folder = tempfile.gettempdir()

    def delete_temp_files(self, folder):
        for item in os.listdir(folder):
            item_path = os.path.join(folder, item)
            try:
                if os.path.isfile(item_path):
                    os.unlink(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
            except Exception as e:
                print(f"Failed to delete {item_path}: {e}")

    def run_clean_temp(self):
        print("Cleaning Temporary Files...")
        self.delete_temp_files(self.temp_folder)
        print("Temporary Files Cleanup Completed.")
