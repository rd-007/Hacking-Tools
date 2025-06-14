"""
IP Address Location Tracker - Educational Tool

This script retrieves geolocation information for a given IP address using a public API.
It demonstrates how IP-based location tracking works and highlights privacy considerations.

Usage:
    python ip_location_tracker.py

Notes:
- Use this tool responsibly and respect privacy laws.
- This script uses the free ipinfo.io API for demonstration purposes.
- It works for public IP addresses; private/local IPs will not return meaningful location data.

Author: Ethical Security Research Assistant
License: MIT License
"""

import requests

def get_ip_location(ip: str):
    """
    Queries the ipinfo.io API to get location data for the given IP address.
    """
    url = f"https://ipinfo.io/{ip}/json"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        location = {
            "IP": data.get("ip", "N/A"),
            "Hostname": data.get("hostname", "N/A"),
            "City": data.get("city", "N/A"),
            "Region": data.get("region", "N/A"),
            "Country": data.get("country", "N/A"),
            "Location (lat,lng)": data.get("loc", "N/A"),
            "Organization": data.get("org", "N/A"),
            "Postal": data.get("postal", "N/A"),
            "Timezone": data.get("timezone", "N/A")
        }
        return location
    except requests.RequestException as e:
        print(f"Error retrieving data: {e}")
        return None

def main():
    print("IP Address Location Tracker (Educational Tool)")
    ip = input("Enter the IP address to track (or leave blank for your own IP): ").strip()
    if not ip:
        ip = ""  # Empty string for querying own IP

    location = get_ip_location(ip)
    if location:
        print("\nLocation Information:")
        for key, value in location.items():
            print(f"{key}: {value}")
    else:
        print("Failed to retrieve location information.")

if __name__ == "__main__":
    main()
