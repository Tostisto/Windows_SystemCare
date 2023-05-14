import subprocess
from enum import Enum


class ScanType(Enum):
    FULL = "full"
    QUICK = "quick"

    def __str__(self):
        return self.value

    @staticmethod
    def from_string(s):
        try:
            return ScanType[s.upper()]
        except KeyError:
            raise ValueError()


class WindowsDefenderScanner:
    def __init__(self):
        self.ps_path = "powershell.exe"

    def run_scan(self, scan_type):
        print(f"Running {scan_type.name} scan with Windows Defender...")
        try:
            subprocess.run([self.ps_path, "-Command", f"Start-MpScan -ScanType {scan_type.value}"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Windows Defender scan failed: {e}")
        else:
            print(f"Windows Defender {scan_type.name} scan completed successfully.")
