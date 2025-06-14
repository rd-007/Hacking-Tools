"""
ZIP File Password Cracker (User-Driven)

- This script attempts to brute-force crack a password-protected ZIP file.
- It lets the user input the ZIP file path and wordlist path interactively via the console, then tries passwords from the provided wordlist until the ZIP file is successfully unlocked.

Usage: Run the script and follow prompts.

Notes:
- This tool is strictly for ethical use: recovering passwords of ZIP files you own or have permission to test.
- Ensure the wordlist file contains one password per line.
- The script tries each password sequentially until it finds the correct one or exhausts the list.

"""

import zipfile

def crack_zip(zip_path: str, wordlist_path: str):
    try:
        zip_file = zipfile.ZipFile(zip_path)
    except FileNotFoundError:
        print(f"Error: ZIP file '{zip_path}' not found.")
        return
    except zipfile.BadZipFile:
        print(f"Error: '{zip_path}' is not a valid ZIP file.")
        return

    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            passwords = f.read().splitlines()
    except FileNotFoundError:
        print(f"Error: Password wordlist file '{wordlist_path}' not found.")
        return

    print(f"[*] Starting password cracking on '{zip_path}' using wordlist '{wordlist_path}'")
    print(f"[*] {len(passwords)} passwords to try")

    for idx, password in enumerate(passwords, start=1):
        try:
            # zipfile requires password as bytes
            zip_file.extractall(pwd=password.encode('utf-8'))
            print(f"[+] Password found: '{password}'")
            return
        except RuntimeError:
            # Wrong password causes RuntimeError
            pass
        except zipfile.BadZipFile:
            print("[!] Corrupted ZIP file or wrong password. Exiting.")
            return
        except Exception as e:
            print(f"[!] Unexpected error: {e}")
            return

        if idx % 100 == 0 or idx == len(passwords):
            print(f"[*] Tried {idx} passwords...")

    print("[-] Password not found in wordlist.")

def main():
    print("=== ZIP File Password Cracker ===")
    zip_path = input("Enter the path to the ZIP file: ").strip()
    wordlist_path = input("Enter the path to the password wordlist file: ").strip()

    crack_zip(zip_path, wordlist_path)

if __name__ == "__main__":
    main()

