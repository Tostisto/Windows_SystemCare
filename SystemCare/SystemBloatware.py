import re
import subprocess


class SystemBloatware:

    def get_system_packages_list(self):
        command = 'DISM /Online /Get-ProvisionedAppxPackages | Select-String -Pattern "(?i)Package.*|(?i)Display.*"'
        result = subprocess.run(['powershell', '-Command', command], capture_output=True, text=True)

        lines = result.stdout.split('\n')
        lines = [line for line in lines if line and re.search(r'Package.*|Display.*', line)]

        packages = []

        for i in range(0, len(lines), 2):
            display_name_match = re.search(r'DisplayName : (.+)', lines[i])
            package_name_match = re.search(r'PackageName : (.+)', lines[i + 1])

            if display_name_match and package_name_match:
                display_name = display_name_match.group(1)
                package_name = package_name_match.group(1)
                package = {
                    'displayname': display_name,
                    'packagename': package_name
                }
                packages.append(package)

        return packages

    def remove_system_package(self, package_name):
        command = f'dism /online /remove-provisionedappxpackage /packagename:{package_name}'
        result = subprocess.run(['powershell', '-Command', command], capture_output=True, text=True)
        return result.stdout
