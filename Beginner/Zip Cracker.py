import sys
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
            # wrong password causes RuntimeError: Bad password for file
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
    if len(sys.argv) != 3:
        print("Usage: python zip_password_cracker.py <zipfile_path> <password_wordlist>")
        sys.exit(1)

    zip_path = sys.argv[1]
    wordlist_path = sys.argv[2]

    crack_zip(zip_path, wordlist_path)

if __name__ == "__main__":
    main()

