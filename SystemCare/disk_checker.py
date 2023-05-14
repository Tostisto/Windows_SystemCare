import subprocess


class DiskChecker:
    def __init__(self):
        self.chkdsk_path = "chkdsk"

    def check_disk(self, disks):
        if not disks:
            print("No disk selected.")
            return

        for disk in disks:
            print(f"Checking disk {disk}...")
            try:
                subprocess.run([self.chkdsk_path, disk, "/f"], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Disk check failed for {disk}: {e}")
            else:
                print(f"Disk check completed successfully for {disk}.")
