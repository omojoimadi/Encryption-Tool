## Encryption Tool
A simple encryption and decryption tool built with **Python**, **CustomTkinter** and **Fernet(cryptography library)**.
It lets you encrypt text or files using symmetric encryption


## Features
- Modern GUI built with CustomTkinter

- Encrypt and decrypt text

- Encrypt and decrypt files

- Automatically generated secure encryption keys

- Easy copy/paste and file browsing

- Runs on Windows, macOS, and Linux (as long as Python is installed)

## Requirements
You need to install python and a few libraries
1. Download python from the official site
   
   - [Download Python](https://www.python.org/downloads/)
     
3. Download these these libraries from your terminal or powershell
   
   - ```bash
     pip install customtkinter cryptography

## How to Run
In the project directory

  - ```bash
    python encryption_tool.py
  The UI will open immediately.
  
  ![Screenshot of UI](img/ui_screenshot.png)  


## How it works
This tool uses Fernet, a high-level interface of the cryptography library.

**Fernet:**

- Generates strong symmetric keys

- Ensures messages cannot be read or modified without the correct key

- Uses AES-128 in CBC mode with PKCS7 padding + HMAC for integrity

> Your key is stored (or typed) in the app — keep it safe!
