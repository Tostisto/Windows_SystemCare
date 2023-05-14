import psutil


class DiskInfo:
    @staticmethod
    def get_disk_partitions():
        partitions = psutil.disk_partitions()
        disks = []
        for part in partitions:
            if 'fixed' in part.opts:
                disk = {}
                disk['name'] = part.device
                usage = psutil.disk_usage(part.mountpoint)
                disk['total_size'] = usage.total
                disk['used_space'] = usage.used
                disk['free_space'] = usage.free
                disks.append(disk)
        return disks
