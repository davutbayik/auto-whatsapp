import os
from autoWhatsApp import send_individual_contact, send_multiple_contact
import warnings
warnings.filterwarnings("ignore")

# Message configurations
PHONE_NUMBER = "+905343015153"
PHONE_NUMBERS = ["+905343015153", "+905072634260"]
MESSAGE = "Hello, this is an automated message sent via autoWhatsApp module."
HEADLESS_MODE = True
ATTACHMENTS = os.listdir("assets")

if __name__ == "__main__":
    
    
    send_individual_contact(
        phone_number=PHONE_NUMBER,
        message=MESSAGE,
        headless=HEADLESS_MODE,
        attachments=ATTACHMENTS
    )
    '''

    send_multiple_contact(
        phone_numbers=PHONE_NUMBERS,
        message=MESSAGE,
        headless=HEADLESS_MODE,
        attachments=ATTACHMENTS
    )
    
    '''