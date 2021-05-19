# -*- coding: utf-8 -*-
import smtplib

def send_user_mail(email):
    remitente = "Sorteo <sorteo@dominio.com>"
    destinatario = email
    asunto = "Email de activación de cuenta"
    mensaje = """Hola!<br/> <br/>
    Utilice este link para activar su cuenta <a href="http://localhost:8000/activar/"+email+">Activar</a>
    """

    email = """From: %s
    To: %s
    MIME-Version: 1.0
    Content-type: text/html
    Subject: %s

    %s
    """ % (remitente, destinatario, asunto, mensaje)
    try:
        smtp = smtplib.SMTP('localhost')
        smtp.sendmail(remitente, destinatario, email)
        print("Correo enviado")
    except:
        print("""Error: el mensaje no pudo enviarse.
        Compruebe que sendmail se encuentra instalado en su sistema""")
