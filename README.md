# 📲🤖 Auto WhatsApp 

Automate WhatsApp messaging using Python and Selenium.

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📌 Introduction

**Auto WhatsApp** is a Python-based tool designed to automate the process of sending messages through WhatsApp Web. Utilizing Selenium WebDriver, it simulates user interactions to send messages to specified contacts or groups.

## ✨ Features

- 🤖 Automated sending of messages via WhatsApp Web
- 👥 Support for sending messages to individual or multiple contacts
- ✏️ Customizable message content
- 📎 Allows single or multiple attachments upload
- 🌐 Utilizes Selenium for browser automation

## 📋 Prerequisites
- Python 3.9+
- Selenium 4.28+

## 🛠️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/davutbayik/auto-whatsapp
   cd auto-whatsapp

2. Create and activate a virtual environment (Optional-Recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3. Install the required packages:
   ```bash
   pip install -r requirements.txt

## 🧪 Usage

1. 📝 **Prepare your message and recipients:**
   - Edit `main.py` to specify the message content and list of recipients.

2. 🔗 **Add attachments:**
   - If you have any attachments to include the message, add them to `assets` folder.

3. ▶️ **Run the script:**
   ```bash
   python autoWhatsApp.py
   ```

4. 📲 **Scan the QR Code:**
   - Set `HEADLESS_MODE=False` before the first use of the application.
   - A browser window will open directing to WhatsApp Web.
   - Scan the QR code with your WhatsApp mobile app to log in.
   - After initial QR Scan, the app will automatically logging in to your WhatsApp account unless you delete the connection from your phone.
   - You can set `HEADLESS_MODE=True` for a better experience after an initial successful QR login.

5. 📤 **Automated messaging:**
   - Once logged in, the script will automatically send the specified messages and attachments to the listed contacts one by one.

⚠️ **Important:**
   - Change `SEND_BUTTON_NAME` variable and `PENDING_MARK` in `autoWhatsApp.py` file to your WhatsApp Web account's display language. 
   For example set `SEND_BUTTON_NAME = 'Send'`, `PENDING_MARK = ' Pending '` for English and set `SEND_BUTTON_NAME = 'Gönder'`, `PENDING_MARK = ' Bekliyor '` for Turkish languages.
   If the word not matches to your language then the program may fail.

## 📈 Examples

### 1. Send message to an individual contact:
```python
import os
from autoWhatsApp import send_individual_contact

 send_individual_contact(
     phone_number="+905xxxxxxxxx",
     message="Hello, this is an automated message sent via autoWhatsApp module.",
     headless=True,
     attachments=os.listdir("assets") # Send all the files in the 'assets' folder
 )
```

### 2. Send message to multiple contacts one-by-one:
```python
import os
from autoWhatsApp import send_multiple_contacts

 send_multiple_contacts(
     phone_number=["+905xxxxxxxxx", "+905yyyyyyyyy"]
     message="Hello, this is an automated message sent via autoWhatsApp module.",
     headless=True,
     attachments=os.listdir("assets") # Send all the files in the 'assets' folder
 )
```

## 📄 License

This project is licensed under the terms of the [MIT License](LICENSE).  
You are free to use, modify, and distribute this software as long as you include the original license.

## 📬 Contact

Made with ❤️ by [Davut Bayık](https://github.com/davutbayik) — feel free to reach out via GitHub for questions, feedback, or collaboration ideas.

---

⭐ If you found this project helpful, consider giving it a star!
