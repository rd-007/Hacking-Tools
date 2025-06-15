"""
Wi-Fi Network Information Extractor (Windows)

- This script extracts all saved Wi-Fi network SSIDs and their stored passwords from your Windows system. It uses native Windows commands to retrieve network profiles.

Usage: python wifi_info_extractor.py

Notes:
- Run this script with administrative privileges.
- Use only on systems you own or have explicit permission to audit.
- This script works on Windows only.

"""

import subprocess
import re

def get_saved_wifi_profiles():
    """ Get list of saved Wi-Fi profiles on Windows """
    try:
        output = subprocess.check_output("netsh wlan show profiles", shell=True, text=True, encoding="utf-8")
        profiles = re.findall(r"All User Profile\s*:\s*(.*)", output)
        return [profile.strip() for profile in profiles]
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute command: {e}")
        return []

def get_wifi_password(profile_name: str):
    """ Get the Wi-Fi password for a given profile name """
    try:
        output = subprocess.check_output(f'netsh wlan show profile name="{profile_name}" key=clear', shell=True, text=True, encoding="utf-8")
        password_match = re.search(r"Key Content\s*:\s*(.*)", output)
        if password_match:
            return password_match.group(1).strip()
        else:
            return None  # No password set (open network or key not found)
    except subprocess.CalledProcessError as e:
        print(f"Failed to get password for {profile_name}: {e}")
        return None

def main():
    print("Wi-Fi Network Information Extractor\n")
    profiles = get_saved_wifi_profiles()
    if not profiles:
        print("No Wi-Fi profiles found or unable to retrieve profiles.")
        return

    print(f"Found {len(profiles)} Wi-Fi profiles:\n")

    for profile in profiles:
        password = get_wifi_password(profile)
        if password:
            print(f"SSID: {profile}\nPassword: {password}\n{'-' * 30}")
        else:
            print(f"SSID: {profile}\nPassword: <None or unable to retrieve>\n{'-' * 30}")

if __name__ == "__main__":
    main()
