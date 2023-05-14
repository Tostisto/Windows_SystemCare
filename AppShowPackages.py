import inquirer


class AppShowPackages:
    def __init__(self, packages):
        self.all_packages = packages
        self.sel_packages = [(package['displayname'], package['packagename']) for package in packages]

    def select_packages(self):
        questions = [
            inquirer.Checkbox(
                "packages",
                message="Select packages to remove",
                choices=self.sel_packages,
            ),
        ]

        answers = inquirer.prompt(questions)

        selected_packages = [package for package in self.all_packages if package['packagename'] in answers['packages']]

        return selected_packages
