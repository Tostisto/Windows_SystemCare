import subprocess


class WindowsUpdater:
    def __init__(self):
        self.powershell_path = "powershell.exe"

    def _check_module_installed(self, module_name):
        try:
            subprocess.run([self.powershell_path, "Get-Module", "-ListAvailable", module_name], check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def _install_module(self, module_name):
        try:
            subprocess.run([self.powershell_path, "Install-Module", module_name], check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {module_name} module: {e}")
            return False

    def update_windows(self):
        module_name = "PSWindowsUpdate"
        if not self._check_module_installed(module_name):
            print(f"{module_name} module not found, installing...")
            if not self._install_module(module_name):
                print(f"Failed to install {module_name} module, aborting Windows update.")
                return

        print("Updating Windows...")
        try:
            subprocess.run([self.powershell_path, "Install-WindowsUpdate", "-AcceptAll", "-Verbose"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Windows update failed: {e}")
        else:
            print("Windows update completed successfully.")
