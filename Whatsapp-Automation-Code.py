from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# ====== SETTINGS ======
contacts = [
    ("+1234567890", "Hello Alice! How are you?"),
    ("+1234567890", "Hi Bob! Don't forget our meeting."),
    ("+1234567890", "Hey Carol! Have a great day! 🌸")
]
# CHROME_DRIVER_PATH = r"C:\\Tools\\ChromeDriver\\chromedriver.exe"  # Change path if needed
BRAVE_BINARY_PATH = r"C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"  # Change path if needed
# ====== CONFIGURE BRAVE ======
options = Options()
options.binary_location = BRAVE_BINARY_PATH
# service = Service(CHROME_DRIVER_PATH)
# ====== START SELENIUM ======
driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com")

time.sleep(60)  # Wait for you to scan the QR code and load chats

# ====== SEND MESSAGES ======
for number, message in contacts:
    # Go directly to the chat with the number
    driver.get(f"https://web.whatsapp.com/send?phone={number}&text={message}")
    time.sleep(30)  # Wait for chat to load
    
    # Press Enter to send
    try:
        # Use JavaScript to trigger Enter key in the input box
        driver.execute_script("""
        let inputBox = document.querySelector('[contenteditable="true"][data-tab="10"]');
        if(inputBox){
            inputBox.dispatchEvent(new InputEvent('input', { bubbles: true }));
            let e = new KeyboardEvent('keydown', {key: 'Enter', code: 'Enter', which: 13, keyCode: 13, bubbles: true});
            inputBox.dispatchEvent(e);
        }
        """)
        print(f"✅ Message sent to {number}")
    except:
        print(f"❌ Failed to send message to {number}")
    time.sleep(15)

print("All messages sent successfully!")
driver.quit()
