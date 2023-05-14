import ctypes
import platform


class CheckToRun:
    @staticmethod
    def check_system():
        if platform.system() != "Windows":
            print("This script is only for Windows.")
            exit(1)

    @staticmethod
    def check_admin():
        if not ctypes.windll.shell32.IsUserAnAdmin():
            print("This script must be run as administrator.")
            exit(1)
