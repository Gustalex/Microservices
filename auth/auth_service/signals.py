from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_service_user(sender, **kwargs):
    if sender.name == "auth_service":
        User = get_user_model()
        username = settings.SERVICE_USER
        password = settings.SERVICE_PASSWORD
        email = settings.SERVICE_EMAIL

        if not User.objects.filter(username=username).exists():
            User.objects.create_user(
                username=username,
                email=email,
                password=password,
                is_staff=True,
                is_superuser=True
            )
            print(f"Usuário de serviço '{username}' criado com sucesso!")
