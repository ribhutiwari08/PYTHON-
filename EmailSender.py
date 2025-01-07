import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email Sending Function
def send_email():
    sender_email = entry_sender.get()
    password = entry_password.get()
    recipient_email = entry_recipient.get()
    subject = entry_subject.get()
    message_body = text_message.get("1.0", tk.END)

    if not (sender_email and password and recipient_email and subject and message_body):
        messagebox.showwarning("Warning", "All fields must be filled out.")
        return

    # Set up the email content
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message_body, 'plain'))

    try:
        # Connect to the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Enable TLS encryption
            server.login(sender_email, password)
            server.send_message(msg)
            messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email.\n\n{e}")

# GUI Setup
app = tk.Tk()
app.title("Email Sender")
app.geometry("500x400")
app.config(bg="lightgray")

# Sender Email
tk.Label(app, text="Sender Email:", bg="lightgray").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_sender = tk.Entry(app, width=30)
entry_sender.grid(row=0, column=1, padx=10, pady=5)

# Password
tk.Label(app, text="Password:", bg="lightgray").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_password = tk.Entry(app, show="*", width=30)
entry_password.grid(row=1, column=1, padx=10, pady=5)

# Recipient Email
tk.Label(app, text="Recipient Email:", bg="lightgray").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_recipient = tk.Entry(app, width=30)
entry_recipient.grid(row=2, column=1, padx=10, pady=5)

# Subject
tk.Label(app, text="Subject:", bg="lightgray").grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_subject = tk.Entry(app, width=30)
entry_subject.grid(row=3, column=1, padx=10, pady=5)

# Message
tk.Label(app, text="Message:", bg="lightgray").grid(row=4, column=0, padx=10, pady=5, sticky="ne")
text_message = tk.Text(app, width=40, height=10)
text_message.grid(row=4, column=1, padx=10, pady=5)

# Send Button
tk.Button(app, text="Send Email", command=send_email, bg="blue", fg="white", width=15).grid(row=5, column=1, pady=10)

# Run the app
app.mainloop()
