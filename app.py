
from flask import Flask, request, send_file, render_template
import pandas as pd
import qrcode
import uuid
import os
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
EXCEL_FILE = "user_data.xlsx"

def send_email_with_qr(email, qr_filename):
    msg = EmailMessage()
    msg["Subject"] = "Your QR Code"
    msg["From"] = "add your email"
    msg["To"] = email
    msg.set_content("Thank you for registering. Attached is your QR code.")

    with open(qr_filename, "rb") as f:
        qr_data = f.read()
        msg.add_attachment(qr_data, maintype="image", subtype="png", filename=qr_filename)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("add your email", "gamil app code")
        smtp.send_message(msg)

@app.route('/')
def index():
    return render_template("form.html")

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']

    new_entry = pd.DataFrame([[name, email, phone]], columns=["Name", "Email", "Phone"])

    if os.path.exists(EXCEL_FILE):
        existing_df = pd.read_excel(EXCEL_FILE)
        if ((existing_df['Email'] == email) | (existing_df['Phone'] == phone)).any():
            return render_template("already_registered.html")
    else:
        existing_df = pd.DataFrame(columns=["Name", "Email", "Phone", "QR_ID", "Used"])

    unique_id = str(uuid.uuid4())
    new_row = pd.DataFrame([[name, email, phone, unique_id, "unused"]],
                           columns=['Name', 'Email', 'Phone', 'QR_ID', 'Used'])
    updated_df = pd.concat([existing_df, new_row], ignore_index=True)
    updated_df.to_excel(EXCEL_FILE, index=False)

    img = qrcode.make(f"http://localhost:5000/verify/{unique_id}")
    qr_path = f"{unique_id}.png"
    img.save(qr_path)

    send_email_with_qr(email, qr_path)
    os.remove(qr_path)

    return "QR Code has been sent to your email."

@app.route('/verify/<qr_id>')
def verify(qr_id):
    if not os.path.exists(EXCEL_FILE):
        return render_template("verify_invalid.html")

    df = pd.read_excel(EXCEL_FILE)
    match = df[df['QR_ID'] == qr_id]

    if match.empty:
        return render_template("verify_invalid.html")

    if match.iloc[0]['Used'] == "used":
        return render_template("verify_used.html")

    df.loc[df['QR_ID'] == qr_id, 'Used'] = "used"
    df.to_excel(EXCEL_FILE, index=False)
    return render_template("verify_success.html")

if __name__ == "__main__":
    app.run(debug= True)
