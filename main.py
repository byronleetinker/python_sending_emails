import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# My email address.
sender_email_id = 'byronleetinker03@gmail.com'
# People who will be receiving emails.
receiver_email_id = ['aneeqahjones2@gmail.com', 'godwin@lifechoices.co.za', 'thapelo@lifechoices.co.za',
                     'byrontobyleetinker@gmail.com']
# Input for users passwords.
password = input("Enter your password")
# Message from myself
subject = "Greetings"

# Indicating who is sending the email, who will receive it and what the message is.
msg = MIMEMultipart()
msg['From'] = sender_email_id
msg['To'] = ','.join(receiver_email_id)
msg['Subject'] = subject

# The message that all the receivers will get.
body = "Hi.\n"
body = body + "Have an awesome day"

msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()
s = smtplib.SMTP('smtp.gmail.com', 587)
# Start TLS for security.
s.starttls()
# Authorization.
s.login(sender_email_id, password)


# Sending the email.
s.sendmail(sender_email_id, receiver_email_id, text)
# Ending the session.
s.quit()
