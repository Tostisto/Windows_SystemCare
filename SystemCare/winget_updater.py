import subprocess
from SystemCare.update_type import UpdateType


class WingetUpdater:
    def __init__(self):
        self.winget_path = "winget.exe"

    def update_packages(self, update_type=UpdateType.ALL):
        if update_type == UpdateType.ALL:
            self._update_all_packages()
        elif update_type == UpdateType.UNKNOWN:
            self._update_all_packages(include_unknown=True)
        else:
            print("Invalid update type.")

    def _update_all_packages(self, include_unknown=False):
        print("Updating all packages...")
        command = [self.winget_path, "upgrade", "--all"]
        if include_unknown:
            command.append("--include-unknown")
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Winget package update failed: {e}")
        else:
            print("Winget package update completed successfully.")
