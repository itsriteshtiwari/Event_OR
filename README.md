# Event_OR

# QR Event Ticketing System
A lightweight, Flask-based event registration and ticketing application inspired by platforms like BookMyShow. This system allows users to register for an event, automatically receives a unique QR code ticket via email, and provides a secure scanning mechanism for event organizers to verify and validate entry.

## 🚀 Features
- **User Registration:** Simple web form for attendees to enter their name, email, and phone number.
- **Duplicate Prevention:** Checks existing records to ensure the same email or phone number cannot register twice.
- **Dynamic QR Code Generation:** Generates a unique, UUID-based QR code for every successful registration.
- **Automated Email Delivery:** Automatically emails the generated QR code ticket directly to the user's inbox as a PNG attachment.
- **Single-Use Verification:** Event organizers can scan the QR code to grant entry. The system marks the ticket as "used" to prevent multiple entries with the same QR code.
- **Excel Database:** Stores all registration and validation data neatly in an Excel file (user_data.xlsx) for easy access and portability.

## 🛠️ Tech Stack
- **Backend:** Python, Flask
- **Data Handling:** Pandas, Openpyxl (Excel read/write)
- **QR Generation:** `qrcode` library
- **Email Handling:** Built-in `smtplib` and `email.message`

<img width="1046" height="668" alt="image" src="https://github.com/user-attachments/assets/33f4a201-4f30-4530-9786-7b8d36a9a818" />
This how form looks like
