import platform
import os
import subprocess
import sys

UDEV_RULE_PATH = '/etc/udev/rules.d/53-adi-m1k-usb.rules'
UDEV_RULE_CONTENTS = '''\
# allow "plugdev" group read/write access to ADALM1000 devices
SUBSYSTEM=="usb", ATTRS{idVendor}=="064b", ATTRS{idProduct}=="784c", MODE="0664", GROUP="plugdev", TAG+="uaccess"
# allow "plugdev" group read/write access to ADALM1000 devices in SAM-BA mode
SUBSYSTEM=="usb", ATTRS{idVendor}=="03eb", ATTRS{idProduct}=="6124", MODE="0664", GROUP="plugdev", TAG+="uaccess"
'''

def get_superuser_command():
    if os.system("which doas > /dev/null 2>&1") == 0:
        return "doas"
    elif os.system("which sudo > /dev/null 2>&1") == 0:
        return "sudo"
    else:
        return None

def main():
    try:
        if platform.system().lower() != "linux":
            print("This operation is only needed on Linux systems.")
            return

        superuser = get_superuser_command()
        if not superuser:
            print("Neither 'doas' nor 'sudo' found. This script requires superuser privileges.")
            return

        if os.path.exists(UDEV_RULE_PATH):
            print(f"Rules file already exists at {UDEV_RULE_PATH}.")
            reload = input("(needs root auth) Do you want to reload udev rules? (y/n): ").strip().lower()
            if reload == "y":
                reload_udev_rules(superuser)
            return

        ans = input(f"(needs root auth) {UDEV_RULE_PATH} not found. Do you want to install it? (y/n): ").strip().lower()
        if ans == "y":
            # Write the file with user privileges first
            with open('/tmp/53-adi-m1k-usb.rules', 'w') as f:
                f.write(UDEV_RULE_CONTENTS)
            subprocess.run([superuser, 'mv', '/tmp/53-adi-m1k-usb.rules', UDEV_RULE_PATH], check=True)
            subprocess.run([superuser, 'chmod', '644', UDEV_RULE_PATH], check=True)
            print(f"Installed rules to {UDEV_RULE_PATH}.")
            reload_udev_rules(superuser)
        else:
            print("Installation aborted by user.")
    except Exception as e:
        print(f"Error: {e}")

def reload_udev_rules(superuser):
    try:
        print("Reloading udev rules...")
        subprocess.run([superuser, 'udevadm', 'control', '--reload'], check=True)
        subprocess.run([superuser, 'udevadm', 'trigger'], check=True)
        print("udev rules reloaded successfully.")
    except Exception as e:
        print(f"Failed to reload udev rules: {e}")

if __name__ == "__main__":
    main()
