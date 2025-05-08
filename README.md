# 🚀 Auto WhatsApp 

Automate WhatsApp messaging using Python and Selenium.

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📌 Introduction

**Auto WhatsApp** is a Python-based tool designed to automate the process of sending messages through WhatsApp Web. Utilizing Selenium WebDriver, it simulates user interactions to send messages to specified contacts or groups.

## ✨ Features

- 🤖 Automated sending of messages via WhatsApp Web
- 👥 Support for sending messages to multiple contacts or groups
- ✏️ Customizable message content
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

1. 🖥️ **Enter your pc user name:**
   - Edit `PC_USER_NAME` parameter for automatic logins

2. 📝 **Prepare your message and recipients:**
   - Edit `main.py` to specify the message content and list of recipients.

3. 🔗 **Add attachments:**
   - If you have any attachments to include the message, add them to `assets` folder.

4. ▶️ **Run the script:**
   ```bash
   python autoWhatsApp.py
   ```

5. 📲 **Scan the QR Code:**
   - A browser window will open directing to WhatsApp Web.
   - Scan the QR code with your WhatsApp mobile app to log in.
   - After initial QR Scan, the app will automatically logging in to your WhatsApp account unless you delete the connection from your phone.

6. 📤 **Automated messaging:**
   - Once logged in, the script will automatically send the specified messages and attachments to the listed contacts one by one.

## 📄 License

This project is licensed under the terms of the [MIT License](LICENSE).  
You are free to use, modify, and distribute this software as long as you include the original license.

## 📬 Contact

Made with ❤️ by [Davut Bayık](https://github.com/davutbayik) — feel free to reach out via GitHub for questions, feedback, or collaboration ideas.

---

⭐ If you found this project helpful, consider giving it a star!
