"""
Basic NFC Tag Reader using nfcpy (Educational Tool)

- This script listens for NFC tags and reads their UID and NDEF records.
- Requires an NFC reader compatible with nfcpy.

Usage: python nfc_reader.py

Notes:
- Use only with NFC tags and devices you have permission to interact with.
- Requires installation of nfcpy: pip install nfcpy
- Hardware needed: USB NFC reader like ACR122U

"""

import nfc

def on_connect(tag):
    print("NFC tag detected!")
    print(f"Tag UID: {tag.identifier.hex()}")
    if tag.ndef:
        print("NDEF Records:")
        for record in tag.ndef.records:
            print(f" - {record.type}: {record.pretty()}")
    else:
        print("No NDEF records found.")
    return True  # Disconnect after reading

def main():
    try:
        with nfc.ContactlessFrontend('usb') as clf:
            print("Waiting for NFC tag...")
            clf.connect(rdwr={'on-connect': on_connect})
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
