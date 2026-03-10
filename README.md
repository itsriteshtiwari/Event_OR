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

## ⚙️ Setup and Installation
### 1. Clone the repository
```
git clone https://github.com/itsriteshtiwari/qr-event.git
cd qr-event
```
### 2. Create a virtual environment
```
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
### 3. Install the required dependencies
```
pip install flask pandas qrcode openpyxl
```
### 4. Configure Email Credentials
Update the `send_email_with_qr` function in `app.py` with your sender email and an App Password.
### 5. Run the application
```
python app.py
```

# 📱 How It Works
1. **Register:** A user visits the home page and submits their details.
2. **Receive Ticket:** The backend creates a new entry in `user_data.xlsx` with a unique UUID, generates a QR code linking to a validation URL (`/verify/<uuid>`), and emails it to the user.
3. **Scan at Event:** At the event entrance, the organizer scans the QR code using any standard QR scanner (which opens the link on the local server/network).
4. **Validation:** If valid and unused, the system grants access and marks the ticket as `used` in the Excel database.
   -If already used, the system displays an "already scanned" warning.
   -If invalid, the system rejects the entry.

<img width="1046" height="668" alt="image" src="https://github.com/user-attachments/assets/33f4a201-4f30-4530-9786-7b8d36a9a818" />
This how form looks like
