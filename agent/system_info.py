import platform
import psutil


def get_system_info():
    return {
        "os": platform.system(),
        "os_version": platform.release(),
        "hostname": platform.node(),
        "interfaces": list(psutil.net_if_addrs().keys()),
    }
