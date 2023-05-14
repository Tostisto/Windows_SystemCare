import subprocess


class Cleanup:
    def __init__(self):
        self.cleanmgr_path = "cleanmgr.exe"

    def run_cleanup(self):
        print("Running Disk Cleanup...")
        try:
            subprocess.run([self.cleanmgr_path, "/sagerun:1"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Disk Cleanup failed: {e}")
        else:
            print("Disk Cleanup completed successfully.")
