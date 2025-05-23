import os
from autoWhatsApp import send_individual_contact, send_multiple_contacts
import warnings
warnings.filterwarnings("ignore") # Silence warnings

# Message configurations
PHONE_NUMBER = "+905xxxxxxxxx" # Edit phone numbers
PHONE_NUMBERS = ["+905xxxxxxxxx", "+905xxxxxxxxx"] # Edit phone numbers
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
    send_multiple_contacts(
        phone_numbers=PHONE_NUMBERS,
        message=MESSAGE,
        headless=HEADLESS_MODE,
        attachments=ATTACHMENTS
    )
    '''
