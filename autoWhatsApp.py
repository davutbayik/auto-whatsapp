import os
import time
import re
import logging
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Validates and normalizes an international phone numbers
def is_valid_phone_number(phone_number):
 
    # Remove spaces and dashes
    cleaned = re.sub(r'[\s\-]', '', phone_number)
    
    # Match international format: + followed by 10-15 digits
    pattern = re.compile(r'^\+\d{10,15}$')
    return bool(pattern.match(cleaned))

# Configure logging
os.makedirs("assets", exist_ok=True)
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("logs/auto_whatsapp_logs.log", mode='a')
    ]
)

class autoWhatsApp(): # Custom class for automating whatsapp

    def __init__(self, headless=True):

        # Setup Chrome options
        options = webdriver.ChromeOptions()

        current_dir_path = os.getcwd()
        profile = os.path.join(current_dir_path, "profile", "wpp")
        
        # Copy chrome profile folder to enable automatic logins after first QR scan
        options.add_argument(f"user-data-dir={profile}")
        
        options.add_argument("--start-maximized")
        options.add_argument('--log-level=3')
        
        if headless == True:
            options.add_argument('--headless=new') # Use headless browser

        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 100000) # Wait before timeout exception
        self.logout_wait = WebDriverWait(self.driver, 60) # Wait until page loads anc checks whether account is logged out
        self.driver.get(f"https://web.whatsapp.com") # Open chat for the given number

    def open_chat(self, number):
        self.driver.get(f"https://web.whatsapp.com/send?phone='{number}'") # Open chat for the given number

    def write_text(self, message):
        message_box = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@tabindex='10']"))) # Find the message box
        message_box.send_keys(Keys.CONTROL + "a") # Select all previous messages if any (from template messages etc.)
        time.sleep(0.25)

        message_box.send_keys(Keys.DELETE) # Delete all previous messages if any		

        if type(message) == list:
            for msg in message:
                message_box.send_keys(msg) # Write messages line by line by sending as a list of strings
                time.sleep(0.5)

                message_box.send_keys(Keys.SHIFT + Keys.ENTER) # Pass to a new line
                time.sleep(0.5)
        else:
            message_box.send_keys(message) # Write message directly in one line by sending as a string

    def upload_file(self, attachments):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[@data-icon='plus-rounded']"))).click() # Click the clip symbol
        time.sleep(0.5)
    
        for attachment in attachments:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys(attachment) # Add file to the inputs
            time.sleep(0.5)
        
        time.sleep(2)

        #self.wait.until(EC.invisibility_of_element_located((By.TAG_NAME, "circle")))

    def send_message(self):
    
        try:
            self.driver.find_element(By.XPATH, "//button[@aria-label='Send']").click() # Click send text button
        except:
            self.driver.find_element(By.XPATH, "//div[@aria-label='Send']").click() # Click send file button

        time.sleep(2)
        self.wait.until(EC.invisibility_of_element_located((By.XPATH, "//span[@aria-label=' Pending ']"))) # Wait until sending (pending) icon disappears

    def checkLogout(self):
    
        try:
            self.logout_wait.until(EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Scan this QR code to link a device!"]')))
            return True

        except:
            return False

# Functions for sending message to the custom class
def send_individual_contact(phone_number: str, message: str, headless: str, attachments: list=[]):

    if type(phone_number) == str:
        pass
    else:
        logging.error("Please give a single phone number! Process ended.")
        return None

    if is_valid_phone_number(phone_number):
        # If an attachment will be sent, put it into 'assets' folder
        if attachments:
            attachments = [os.path.join(os.getcwd(), "assets", file_name) for file_name in attachments] # Convert files to their absolute path

        autoWhatsApp_client = autoWhatsApp(headless=headless) # Initialize a autoWhatsApp client

        autoWhatsApp_client.open_chat(phone_number)# Open a chat for the given phone number
        while True: # While loop in case WhatsApp acoount is logged out and needed to scan a qr code

            if autoWhatsApp_client.checkLogout(): # Check if whether WhatsApp Web account is closed
                logging.warning('''Whatsapp closed on the browser. Please rerun in browser mode (HEADLESS_MODE=False) and scan the QR code!''')
                time.sleep(5)
                
            else:
                logging.info("Successfully logged in to Whatsapp!")
                time.sleep(1)
                
                # Eliminate 'A fresh look for WhatsApp Web' popup window if occurs
                try:
                    popup = autoWhatsApp_client.driver.find_element(By.CLASS_NAME, "x78zum5")
                    popup.find_element(By.TAG_NAME, "button").click()
                    time.sleep(1)
                except:
                    pass
                
                autoWhatsApp_client.open_chat(phone_number)
                
                # Write text messages (string or a list of strings)
                autoWhatsApp_client.write_text(message)

                # Add files if any
                if attachments:
                    autoWhatsApp_client.upload_file(attachments) # Upload a file (image, document etc.)
                
                # Send message
                try:
                    autoWhatsApp_client.send_message() # Send the message
                    logging.info(f"Message successfully sent to number: {phone_number} with {len(attachments)} attachment(s).")
                except:
                    logging.error(f"Error while sending message to number: {phone_number}")

                autoWhatsApp_client.driver.close() # Close the chromedriver
                break   
    else:
        logging.error(f"Phone number {phone_number} is not valid! Process ended.")

def send_multiple_contacts(phone_numbers: list, message: str, headless: str, attachments: list=[]):

    if type(phone_numbers) == list:
        pass
    else:
        logging.error("Please give a list of phone numbers for multiple messaging! Process ended.")
        return None

    # If an attachment will be sent, put it into 'assets' folder
    if attachments:
        attachments = [os.path.join(os.getcwd(), "assets", file_name) for file_name in attachments] # Convert files to their absolute path

    autoWhatsApp_client = autoWhatsApp(headless=headless) # Initialize a autoWhatsApp client

    autoWhatsApp_client.open_chat(phone_numbers[0]) # Open a chat for the given phone number
    while True: # While loop in case WhatsApp acoount is logged out and needed to scan a qr code

        if autoWhatsApp_client.checkLogout(): # Check if whether WhatsApp Web account is closed
            logging.warning('''Whatsapp closed on the browser. Please rerun in browser mode (HEADLESS_MODE=False) and scan the QR code!''')
            time.sleep(5)
            
        else:
            logging.info("Successfully logged in to Whatsapp!")
            time.sleep(1)
            
            # Eliminate 'A fresh look for WhatsApp Web' popup window if occurs
            try:
                popup = autoWhatsApp_client.driver.find_element(By.CLASS_NAME, "x78zum5")
                popup.find_element(By.TAG_NAME, "button").click()
                time.sleep(1)
            except:
                pass
            
            for phone_number in phone_numbers:
                if is_valid_phone_number(phone_number):
                    
                    autoWhatsApp_client.open_chat(phone_number)
                    
                    # Write text messages (string or a list of strings)
                    autoWhatsApp_client.write_text(message)

                    # Add files if any
                    if attachments:
                        autoWhatsApp_client.upload_file(attachments) # Upload a file (image, document etc.)
                    
                    # Send message
                    try:
                        autoWhatsApp_client.send_message() # Send the message
                        logging.info(f"Message successfully sent to number: {phone_number} with {len(attachments)} attachment(s).")
                    except:
                        logging.error(f"Error while sending message to number: {phone_number}")
                else:
                    logging.error(f"The phone number: {phone_number} is not valid! Passing by.")
        
            autoWhatsApp_client.driver.close() # Close the chromedriver
            break
