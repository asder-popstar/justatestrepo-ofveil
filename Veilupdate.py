import socket
import threading
import rsa
import base64
import os
import time
import sys
import wave
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from colorama import Fore, Style, init
import pyaudio
from stegano import lsb
import bluetooth
import torpy
import secrets
import hashlib
import json
from PyQt5 import QtWidgets
import subprocess
import random

# Initialize Colorama
init()

def secure_wipe(directory):
    print(f"[+] Securely wiping {directory}...")
    for root, dirs, files in os.walk(directory, topdown=False):
        for name in files:
            file_path = os.path.join(root, name)
            try:
                with open(file_path, "ba+") as f:
                    length = os.path.getsize(file_path)
                    f.write(os.urandom(length))
                os.remove(file_path)
                print(f"[+] Wiped: {file_path}")
            except Exception as e:
                print(f"[-] Error wiping {file_path}: {e}")
        for name in dirs:
            dir_path = os.path.join(root, name)
            try:
                os.rmdir(dir_path)
                print(f"[+] Deleted Directory: {dir_path}")
            except Exception as e:
                print(f"[-] Error deleting {dir_path}: {e}")

def wipe_system():
    directories = ["~/Downloads", "~/Pictures", "~/Documents", "~/Logs", "~/Desktop"]
    for directory in directories:
        secure_wipe(os.path.expanduser(directory))
    print("[+] System wipe completed.")

ASCII_ART = f"""
{Fore.GREEN}__     __   _ _ 
\ \   / /__(_) |
 \ \ / / _ \ | |
  \ V /  __/ | |
   \_/ \___|_|_|{Style.RESET_ALL}
"""

def display_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print(ASCII_ART)
    print(f"{Fore.CYAN}\n[ Secure Communication Suite ]{Style.RESET_ALL}")
    print("1. Start as Server")
    print("2. Start as Client")
    print("3. Secure File Transfer")
    print("4. Stealth Messaging (Steganography)")
    print("5. Encrypted Voice Call")
    print("6. Mesh Network Messaging")
    print("7. Enable Tor Anonymity")
    print("8. Spoof MAC Address")
    print("9. Randomize Hostname")
    print("10. Disable Tracking")
    print("11. Secure Wipe System")
    print("12. Exit")
    choice = input("Select an option (1-12): ")
    return choice

def main():
    while True:
        choice = display_menu()
        if choice == '1':
            server()
        elif choice == '2':
            server_ip = input("Enter server IP: ")
            client(server_ip)
        elif choice == '3':
            print("[+] Secure File Transfer Coming Soon...")
        elif choice == '4':
            print("[+] Stealth Messaging Coming Soon...")
        elif choice == '5':
            print("[+] Encrypted Voice Call Coming Soon...")
        elif choice == '6':
            mesh_network()
        elif choice == '7':
            tor_setup()
        elif choice == '8':
            spoof_mac()
        elif choice == '9':
            randomize_hostname()
        elif choice == '10':
            disable_tracking()
        elif choice == '11':
            wipe_system()
        elif choice == '12':
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
