import pywhatkit
# Phone_Number = "+44 7553 409888"
# Message = "Hello Rahul"
# time_hour = 1
# time_minute = 47
# time_out = 30
# tab_close = True
# close_time = 59
# pywhatkit.sendwhatmsg(Phone_Number, Message, time_hour, time_minute, time_out, tab_close, close_time)



# contacts = [
#     ("+447884826027", "Hello Alice! How are you?"),
#     ("+447760513276", "Hi Bob! Don't forget our meeting."),
#     ("+447553409888", "Hey Carol! Have a great day! 🌸")
# ]

# # Time to send messages (24-hour format)
# hour = 2
# minute = 23

# for number, message in contacts:
#     pywhatkit.sendwhatmsg(number, message, hour, minute, wait_time=30, tab_close=True, close_time=59)


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.parse
from selenium.webdriver.common.keys import Keys
import time

# ====== SETTINGS ======
contacts = [
    ("+447760513276", "Hello Alice! How are you?"),
    ("+919182242898", "Hi Bob! Don't forget our meeting."),
    ("+447884826027", "Hey Carol! Have a great day! 🌸")
]

# Path to ChromeDriver (download from https://chromedriver.chromium.org/)
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
    # try:
    #     # Wait until the green send button is clickable
    #     send_button = WebDriverWait(driver, 30).until(
    #         EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="Message"]'))
    #     )

    #     # Wait for send button and click it
    #     send_button = WebDriverWait(driver, 30).until(
    #         EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Send"]'))
    #     )
        # send_button.click()
        print(f"✅ Message sent to {number}")
    except:
        print(f"❌ Failed to send message to {number}")
    time.sleep(15)

print("All messages sent successfully!")
driver.quit()