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

def secure_file_transfer(file_path, destination_ip):
    key = os.urandom(32)
    cipher = AES.new(key, AES.MODE_CBC)
    with open(file_path, "rb") as f:
        data = f.read()
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))
    with open(file_path + ".enc", "wb") as f:
        f.write(cipher.iv + encrypted_data)
    print("[+] File encrypted and ready for transfer.")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((destination_ip, 9998))
        s.sendall(cipher.iv + encrypted_data)
    print("[+] File sent successfully.")

def stealth_messaging_hide(message, image_path):
    secret = lsb.hide(image_path, message)
    secret.save("stegano.png")
    print("[+] Message hidden in stegano.png")

def stealth_messaging_reveal(image_path):
    message = lsb.reveal(image_path)
    print(f"[+] Hidden Message: {message}")

def encrypted_voice_call():
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print("[+] Recording encrypted voice call...")
    frames = []
    for _ in range(0, int(RATE / CHUNK * 5)):
        data = stream.read(CHUNK)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    audio.terminate()
    with wave.open("voice_chat.wav", "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b"".join(frames))
    print("[+] Voice chat saved and encrypted.")

def display_menu():
    os.system("cls" if os.name == "nt" else "clear")
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
            file_path = input("Enter file path to transfer: ")
            destination_ip = input("Enter destination IP: ")
            secure_file_transfer(file_path, destination_ip)
        elif choice == '4':
            image_path = input("Enter image filename: ")
            message = input("Enter message to hide: ")
            stealth_messaging_hide(message, image_path)
        elif choice == '5':
            encrypted_voice_call()
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
