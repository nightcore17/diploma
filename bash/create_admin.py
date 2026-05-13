import os
import sys
import django

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bash.settings')
django.setup()

from django.contrib.auth.models import User

# Удаляем всех старых пользователей
User.objects.all().delete()

# Создаём нового админа
User.objects.create_superuser(
    username='admin',
    email='admin@example.com',
    password='123'
)

print('✅ Админ создан!')
print('   Логин: admin')
print('   Пароль:123')