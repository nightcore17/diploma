import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bash.settings')
django.setup()

from django.contrib.auth.models import User

username = 'admin'
password = '123'
email = ''

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f"✅ Суперпользователь '{username}' создан с паролем '{password}'")
else:
    print(f"⚠️ Пользователь '{username}' уже существует")