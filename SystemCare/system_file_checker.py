import subprocess


class SystemFileChecker:
    def __init__(self):
        self.sfc_path = "sfc.exe"
        self.dism_path = "dism.exe"

    def check_system_files(self):
        print("Checking system files...")
        try:
            subprocess.run([self.sfc_path, "/scannow"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"System file check failed: {e}")
        else:
            print("System file check completed successfully.")

    def check_and_repair_online(self):
        print("Checking and repairing online components...")
        try:
            subprocess.run([self.dism_path, "/Online", "/Cleanup-Image", "/RestoreHealth"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Online component check and repair failed: {e}")
        else:
            print("Online component check and repair completed successfully.")
