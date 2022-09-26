
import email.message
import mimetypes
import os.path
import smtplib

def generate(sender, recipient, subject, body, attachments):
  """Creates an email with an attachement."""
  # Basic Email formatting
  message = email.message.EmailMessage()
  message["From"] = sender
  message["To"] = recipient
  message["Subject"] = subject
  message.set_content(body)

  for attachment_path in attachments:
    # Process the attachment and add it to the email
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)

    with open(attachment_path, 'rb') as ap:
      message.add_attachment(ap.read(),
                            maintype=mime_type,
                            subtype=mime_subtype,
                            filename=attachment_filename)

  return message

def send(message,sender,password):
  """Sends the message to the configured SMTP server."""
  mail_server = smtplib.SMTP_SSL('smtp.gmail.com',465)
  mail_server.login(sender, password)
  mail_server.send_message(message)
  mail_server.quit()