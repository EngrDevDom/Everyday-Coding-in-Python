''' Send an Email using Python '''

import smtplib

smtp_session = smtplib.SMTP('smtp.gmail.com', 587)
smtp_session.starttls()

smtp_session.login("sender_email", "sender_password")
msg = "Your Message Here!"
smtp_session.sendmail("sender_email", "receiver_email", msg)
smtp_session.quit()

