import smtplib               
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import credencial
import aniversariantes
from datetime import date, datetime
import time
import schedule

hoje = date.today()

def enviar_email():
  
  for nascimentos in aniversariantes.dados:
    nascimento = datetime.strptime(nascimentos["data_niver"], "%d/%m/%Y").date()
    print(f"📅 Data de nascimento - {nascimento.day:02}/{nascimento.month:02}")
      
    if nascimento.day == hoje.day and nascimento.month == hoje.month:
      print("Hoje é dia de festa! Mandando um abraço virtual para {}!🎉".format(nascimentos["nome"]))
      
      with open(nascimentos["imagem"], "rb") as foto:
        photo = MIMEImage(foto.read())

        photo.add_header(
        'Content-ID',
        '<foto_aniversario>')   

      html = f"""
      <!DOCTYPE html>
        <html lang="pt-BR">

        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Animação de Confete</title>
            <style>
              body {{
                  margin: 0;
                  padding: 0;
                  overflow: hidden;
                  background: #A17168;
                  height: 100vh;
                  
              }}
            </style>
        </head>

        <body>
          <div align="center">

          <div style="
            border: 10px solid #CCABA5;
            padding: 5px;
            background-color: #1F0F08;
            width: 300px;">

          <img src="cid:foto_aniversario"
            width="300"
            height="200"
            style="display:block; border-radius:5px;">

          </div>

          <div align="center" style="padding:20px;">
            <h1 style="
                font-family: Arial, sans-serif;
                font-size: 32px;
                color: black;
                margin-bottom: 20px;
                text-align: center;
                line-height: 1.3;
            ">
                Feliz Aniversário {nascimentos["nome"]}!!
            </h1>

            <p style="
                font-family: Arial, sans-serif;
                font-size: 22px;
                color: black;
                text-align: center;
                line-height: 1.5;
                max-width: 500px;
                margin: 0 auto;
            ">
                Quero te desejar muita prosperidade, amor,
                fartura, saúde e alegria para esse novo ciclo!!
                <br><br>
                Pode contar comigo sempre ❤️
            </p>
          </div>

        </body>
      </html>
            """ 


      msg = MIMEMultipart("alternative")
      msg['Subject'] = "Parabéns, {}! Hoje o dia é todo seu!".format(nascimentos['nome'])
      msg['to'] = nascimentos['email']
      msg.attach(MIMEText(html, "html"))
      msg.attach(photo)

      n = smtplib.SMTP('smtp.gmail.com', 587)
      n.starttls()  
      n.login(credencial.Sender, credencial.Password)
      n.sendmail(credencial.Sender, [msg['to']], msg.as_string().encode('utf-8'))
      print("Enviado!\n")   
    
    else :
      print("Nenhum aniversariante hoje 🎈\n")

schedule.every().day.at("00:27").do(enviar_email)
print("Aguardando o horário agendado...")

while True:
  schedule.run_pending()
  time.sleep(60)

