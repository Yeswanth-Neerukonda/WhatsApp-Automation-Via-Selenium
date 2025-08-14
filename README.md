# WhatsApp Automation Script

A **Python automation script** to send messages on **WhatsApp Web** using **Selenium**.  
This script allows sending messages to multiple contacts automatically, without manually pressing Enter or clicking the send button.

---

## Features

- Send messages to multiple contacts automatically.
- Fully automated using **Selenium** and **Brave Browser**.
- Simulates Enter key in chat via JavaScript.
- Compatible with the current WhatsApp Web interface.
- Easy to customize messages and contacts.

---

## Demo Screenshot

*(Add a screenshot of WhatsApp Web with QR scan and message sending here)*

---

## Requirements

- Python 3.x
- [Selenium](https://pypi.org/project/selenium/)
- [Brave Browser](https://brave.com/) (or Chrome)
- ChromeDriver compatible with your Brave/Chrome version

---

## Installation Steps

### 1. Install Python Packages
Install Selenium via pip:
```bash
pip install selenium
2. Download ChromeDriver
Go to ChromeDriver Downloads

Download the version that matches your browser (Brave/Chrome) version.

Extract chromedriver.exe and save it in a known location (e.g., C:\Tools\ChromeDriver\chromedriver.exe).

3. Set Brave/Chrome Path
In your Python script, configure the browser binary path:

python
Copy
Edit
BRAVE_BINARY_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
4. Configure Contacts
Edit the contacts list in the script with the phone numbers (with country code) and messages:

python
Copy
Edit
contacts = [
    ("+1234567890", "Hello Alice! How are you?"),
    ("+1234567890", "Hi Bob! Don't forget our meeting."),
    ("+1234567890", "Hey Carol! Have a great day! 🌸")
]
Usage
Run the script:

bash
Copy
Edit
python WhatsApp_Automation.py
Scan the QR code displayed in Brave Browser to log in to WhatsApp Web.

The script will automatically:

Open each contact’s chat

Pre-fill the message

Send it automatically

Adjusting Delays
Depending on your internet speed and system performance, you might need to adjust the time.sleep() values:

python
Copy
Edit
time.sleep(60)  # Wait for QR code scan
time.sleep(30)  # Wait for chat to load
time.sleep(15)  # Wait between sending messages
Notes & Tips
Ensure your WhatsApp Web session is active before running the script.

Avoid spamming — use responsibly for personal or authorized communications.

If WhatsApp Web updates its interface, check the script selectors (contenteditable input) and adjust as needed.

License
This project is licensed under the MIT License.

Troubleshooting
Issue	Solution
ChromeDriver not found	Check the path to chromedriver.exe in the script
Brave/Chrome not opening	Verify BRAVE_BINARY_PATH points to the correct browser location
Messages not sending	Make sure QR code is scanned and time.sleep() is sufficient
Script fails after WhatsApp update	Inspect the message input box and update the selector [contenteditable="true"][data-tab="10"]

Contributing
Feel free to fork this repository and improve the automation (e.g., parallel sending, scheduling messages, or supporting multiple browsers).

Author
Yeswanth Neerukonda
