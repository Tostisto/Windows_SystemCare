import inquirer
from pprint import pprint


class AppDiskSelector:
    def __init__(self, disk_list):
        self.disk_list = disk_list

    def select_disks(self):
        disk_names = [disk['name'] for disk in self.disk_list]
        questions = [
            inquirer.Checkbox(
                "disks",
                message="Select disks to run actions on",
                choices=disk_names,
            ),
        ]

        selected_disk_names = inquirer.prompt(questions)['disks']
        selected_disks = [disk for disk in self.disk_list if disk['name'] in selected_disk_names]
        return selected_disks
