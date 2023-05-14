from SystemCare.cleanup import Cleanup
from SystemCare.cleantemp import TempCleaner
from SystemCare.defragmentation import Defragmentation
from SystemCare.retrim import Retrim
from SystemCare.diskinfo import DiskInfo
from SystemCare.winget_updater import WingetUpdater
from SystemCare.update_type import UpdateType
from SystemCare.windows_updater import WindowsUpdater
from SystemCare.disk_checker import DiskChecker
from SystemCare.windows_defender_scanner import WindowsDefenderScanner, ScanType
from SystemCare.system_file_checker import SystemFileChecker
from SystemCare.SystemBloatware import SystemBloatware

from AppDiskSelector import AppDiskSelector
from AppTypeSelector import AppTypeSelector
from AppShowPackages import AppShowPackages

import os
from CheckToRun import CheckToRun
from SystemCare.update_type import UpdateType


class ActionParser:
    def __init__(self):
        self.action_map = {
            "cleanup": self.cleanup_function,
            "temp_cleaning": self.temp_cleaning_function,
            "defragmentation": self.defragmentation_class,
            "retrim": self.retrim_class,
            "package_updates": self.package_updates_function,
            "windows_updates": self.windows_updates_function,
            "disk_checking": self.disk_checking_class,
            "defender_scan": self.defender_scan_class,
            "file_checking": self.file_checking_function,
            "bloatware_removal": self.bloatware_removal_function,
        }

    def clean_init_console(self, action_info):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(action_info)

    def parse_and_run_actions(self, selected_actions):
        for action in selected_actions:
            action_function = self.action_map[action['name']]
            self.clean_init_console(action['title'])
            action_function(action)

    def cleanup_function(self, action_info):
        if action_info['requireAdmin'] is True:
            CheckToRun.check_admin()

        disk_cleanup = Cleanup()
        disk_cleanup.run_cleanup()

    def temp_cleaning_function(self, action_info):
        if action_info['requireAdmin'] is True:
            CheckToRun.check_admin()

        temp_cleaner = TempCleaner()
        temp_cleaner.run_clean_temp()

    def defragmentation_class(self, action_info):
        if action_info['requireAdmin'] is True:
            CheckToRun.check_admin()

        defragmentation = Defragmentation()
        disks = DiskInfo.get_disk_partitions()
        selected_disks = AppDiskSelector(disks).select_disks()

        disks_letter = [disk['name'] for disk in selected_disks]
        defragmentation.run_defragmentation(disks_letter)

    def retrim_class(self, action_info):
        if action_info['requireAdmin'] is True:
            CheckToRun.check_admin()

        retrim = Retrim()
        disks = DiskInfo.get_disk_partitions()
        selected_disks = AppDiskSelector(disks).select_disks()

        disks_letter = [disk['name'] for disk in selected_disks]
        retrim.run_retrim(disks_letter)

    def package_updates_function(self, action_info):
        if action_info['requireAdmin'] is True:
            CheckToRun.check_admin()

        if action_info['type']:
            selected_type = AppTypeSelector(action_info['type']).select_types(select_one=True)
            update_type = UpdateType.from_string(selected_type[1])

        package_updater = WingetUpdater()
        package_updater.update_packages(update_type=update_type)

    def windows_updates_function(self, action_info):
        if action_info['requireAdmin'] is True:
            CheckToRun.check_admin()

        windows_updater = WindowsUpdater()
        windows_updater.update_windows()

    def disk_checking_class(self, action_info):
        if action_info['requireAdmin'] is True:
            CheckToRun.check_admin()

        disks = DiskInfo.get_disk_partitions()
        selected_disks = AppDiskSelector(disks).select_disks()
        selected_disks_name = [disk['name'][:2] for disk in selected_disks]

        disk_checker = DiskChecker()
        disk_checker.check_disk(selected_disks_name)

    def defender_scan_class(self, action_info):
        if action_info['requireAdmin'] is True:
            CheckToRun.check_admin()

        if action_info['type']:
            selected_type = AppTypeSelector(action_info['type']).select_types(select_one=True)

            scan_type = ScanType.from_string(selected_type[1])

        scanner = WindowsDefenderScanner()
        scanner.run_scan(scan_type)

    def file_checking_function(self, action_info):
        if action_info['requireAdmin'] is True:
            CheckToRun.check_admin()

        system_file_checker = SystemFileChecker()
        system_file_checker.check_system_files()
        system_file_checker.check_and_repair_online()

    def bloatware_removal_function(self, action_info):
        if action_info['requireAdmin'] is True:
            CheckToRun.check_admin()

        system_bloat = SystemBloatware()
        packages = system_bloat.get_system_packages_list()

        show_packages = AppShowPackages(packages)
        selected_packages = show_packages.select_packages()

        for package in selected_packages:
            system_bloat.remove_system_package(package['packagename'])
