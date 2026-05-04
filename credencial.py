import os
from dotenv import load_dotenv

load_dotenv()

Sender = os.getenv("Quem_Envia")
Password = os.getenv("senha")

#print("Crendenciais ativas")