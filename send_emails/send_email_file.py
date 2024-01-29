import smtplib
import ssl
from email.message import EmailMessage
import imghdr

email_emisor = 'escribe-email-emisor'
email_contrasena = 'escribe-contrasena'
email_receptor = 'escribe-email-receptor'

asunto = 'Revisa mi NUEVO video en YouTube'
cuerpo = """
He publicado un nuevo video en YouTube: https://youtu.be/pxe13_562Vs
"""

em = EmailMessage()
em['From'] = email_emisor
em['To'] = email_receptor
em['Subject'] = asunto
em.set_content(cuerpo)

# Adjuntar archivo
with open('foto.jpg', 'rb') as file:
    file_data = file.read()
    file_tipo = imghdr.what(file.name)
    file_nombre = file.name
em.add_attachment(file_data, filename=file_nombre, subtype=file_tipo, maintype='image')

contexto = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
    smtp.login(email_emisor, email_contrasena)
    smtp.sendmail(email_emisor, email_receptor, em.as_string())
