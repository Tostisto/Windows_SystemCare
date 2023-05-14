import subprocess


class Defragmentation:
    def __init__(self):
        self.defrag_path = "defrag.exe"

    def run_defragmentation(self, drive_letters):
        if not drive_letters:
            print("No disks selected. Defragmentation skipped.")
            return
        for drive_letter in drive_letters:
            print(f"Running Defragmentation on {drive_letter}...")
            try:
                subprocess.run([self.defrag_path, drive_letter, "/U", "/V"], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Defragmentation failed: {e}")
            else:
                print("Defragmentation completed successfully.")
