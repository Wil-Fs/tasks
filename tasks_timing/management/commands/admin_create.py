import os
import django
from django.contrib.auth.models import User
from dotenv import load_dotenv

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seu_projeto.settings')
django.setup()

def create_superuser(username, email, password):
    if User.objects.filter(username=username).exists():
        print('Superusuário já existe')
    else:
        User.objects.create_superuser(username=username, email=email, password=password)
        print('Superusuário criado com sucesso')

# Defina os parâmetros do superusuário
username =  os.getenv('ADMIN_USER')
email = os.getenv('ADMIN_PASSWORD')
password =  os.getenv('ADMIN_EMAIL')

create_superuser(username, email, password)
