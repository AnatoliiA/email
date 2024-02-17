from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import os


def sendemail(receiver, subject, body, imgpath, original_pdf_path_cv, original_pdf_path_resume):
    sender = 'kamarali.work@gmail.com'
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = subject

    # Attach HTML body
    mimetext = MIMEText(body, 'html')
    # noinspection DuplicatedCode
    message.attach(mimetext)

    # Attach PDF mot
    print(f"CV {original_pdf_path_resume}")
    base_pdf_path = original_pdf_path_resume
    try:
        with open(base_pdf_path, 'rb') as file:
            pdf_attachment_file = file.read()
    except FileNotFoundError:
        print(f"File not found: {base_pdf_path}")
        return False

    pdf_payload = MIMEBase('application', 'pdf')
    pdf_payload.set_payload(pdf_attachment_file)
    encoders.encode_base64(pdf_payload)
    pdf_payload.add_header('Content-Disposition', 'attachment', filename=os.path.basename(base_pdf_path))
    message.attach(pdf_payload)

    # Attach PDF CV
    print(f"Letter motivation {original_pdf_path_cv}")
    try:
        with open(original_pdf_path_cv, 'rb') as file:
            pdf_attachment_file = file.read()
    except FileNotFoundError:
        print(f"File not found: {original_pdf_path_cv}")
        return False

    pdf_payload = MIMEBase('application', 'pdf')
    pdf_payload.set_payload(pdf_attachment_file)
    encoders.encode_base64(pdf_payload)
    pdf_payload.add_header('Content-Disposition', 'attachment', filename=os.path.basename(original_pdf_path_cv))
    # noinspection DuplicatedCode
    message.attach(pdf_payload)

    # Attach PDF CV
    original_pdf_path = original_pdf_path_cv
    try:
        with open(original_pdf_path, 'rb') as file:
            pdf_attachment_file = file.read()
    except FileNotFoundError:
        print(f"File not found: {original_pdf_path}")
        return False

    pdf_payload = MIMEBase('application', 'pdf')
    pdf_payload.set_payload(pdf_attachment_file)
    encoders.encode_base64(pdf_payload)
    pdf_payload.add_header('Content-Disposition', 'attachment', filename=os.path.basename(original_pdf_path))
    message.attach(pdf_payload)

    # Attach PDF разрешение вісоты
    #
    original_pdf_path = r"pdf/Travaux en hauteur-07.pdf"
    # noinspection DuplicatedCode
    try:
        with open(original_pdf_path, 'rb') as file:
            pdf_attachment_file = file.read()
    except FileNotFoundError:
        print(f"File not found: {original_pdf_path}")
        return False

    pdf_payload = MIMEBase('application', 'pdf')
    pdf_payload.set_payload(pdf_attachment_file)
    encoders.encode_base64(pdf_payload)
    pdf_payload.add_header('Content-Disposition', 'attachment', filename=os.path.basename(original_pdf_path))
    message.attach(pdf_payload)

    # Attach PDF обучение
    original_pdf_path = r"pdf/FormationCertificatKamarali.pdf"
    # noinspection DuplicatedCode
    try:
        with open(original_pdf_path, 'rb') as file:
            pdf_attachment_file = file.read()
    except FileNotFoundError:
        print(f"File not found: {original_pdf_path}")
        return False

    pdf_payload = MIMEBase('application', 'pdf')
    pdf_payload.set_payload(pdf_attachment_file)
    encoders.encode_base64(pdf_payload)
    pdf_payload.add_header('Content-Disposition', 'attachment', filename=os.path.basename(original_pdf_path))
    message.attach(pdf_payload)

    # Attach image without resizing
    original_image_path = imgpath
    try:
        with open(original_image_path, 'rb') as file:
            attachment_file = file.read()
    except FileNotFoundError:
        print(f"File not found: {original_image_path}")
        return False

    image_payload = MIMEBase('image', 'jpeg')
    image_payload.set_payload(attachment_file)
    encoders.encode_base64(image_payload)
    image_payload.add_header('Content-ID', '<image1>')
    image_payload.add_header('Content-Disposition', 'inline', filename=os.path.basename(original_image_path))
    message.attach(image_payload)

    password = "dbnisuvxyczhbjbh"
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, message.as_string())
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        if os.path.exists(original_pdf_path_cv):
            os.remove(original_pdf_path_cv)
        else:
            print("File does not exist")
        if os.path.exists(original_pdf_path_resume):
            os.remove(original_pdf_path_resume)
        else:
            print("File does not exist")


