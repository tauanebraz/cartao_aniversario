import smtplib               
import email.message
import credencial
import aniversariantes
from datetime import date, datetime

hoje = date.today()

def enviar_email():
    html = """
    <html>
    <head></head>
      <body>
        <p>TESTE -- TESTE<b>TESTE</b></p>
        <p><b>Atenção e apenas um teste</b></p>
        <h1>teste.</h1>
      </body>
    </html>
      """
    
    for nascimentos in aniversariantes.dados:
      nascimento = datetime.strptime(nascimentos["data_niver"], "%d/%m/%Y").date()
      print(f"📅 Data de nascimento - {nascimento.day:02}/{nascimento.month:02}")
      
      if nascimento.day == hoje.day and nascimento.month == hoje.month:
        print("Hoje é dia de festa! Mandando um abraço virtual para {}!🎉".format(nascimentos["nome"]))
        
        msg = email.message.Message()
        msg['Subject'] = "Parabéns, {}! Hoje o dia é todo seu!".format(nascimentos['nome'])
        msg['to'] = nascimentos['email']
        msg.add_header('content-type', 'text/html')
        msg.set_payload(html)

        n = smtplib.SMTP('smtp.gmail.com', 587)
        n.starttls()  
        n.login(credencial.Sender, credencial.Password)
        n.sendmail(credencial.Sender, [msg['to']], msg.as_string().encode('utf-8'))
        print("Enviado!\n")
        
      else :
        print("Nenhum aniversariante hoje 🎈\n")
        
enviar_email()






