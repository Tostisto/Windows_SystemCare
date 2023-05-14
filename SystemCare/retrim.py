import subprocess


class Retrim:
    def __init__(self):
        self.defrag_path = "defrag.exe"

    def run_retrim(self, drive_letters):
        if not drive_letters:
            print("No disks selected. Retrim (SSD Optimization) skipped.")
            return
        for drive_letter in drive_letters:
            print(f"Running Retrim (SSD Optimization) on {drive_letter}...")
            try:
                subprocess.run([self.defrag_path, drive_letter, "/L", "/U", "/V"], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Retrim (SSD Optimization) failed: {e}")
            else:
                print("Retrim (SSD Optimization) completed successfully.")
