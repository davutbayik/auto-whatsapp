import os
from autoWhatsApp import start_auto_whatsapp
import warnings
warnings.filterwarnings("ignore")

# Message configurations
PHONE_NUMBER = "+905xxxxxxxxx"
MESSAGE = "Hello, this is an automated message sent via autoWhatsApp module."
HEADLESS_MODE = False
ATTACHMENTS = os.listdir("assets")

if __name__ == "__main__":
    
    start_auto_whatsapp(
        phone_number=PHONE_NUMBER,
        message=MESSAGE,
        headless=HEADLESS_MODE,
        attachments=ATTACHMENTS
    )
