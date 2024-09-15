from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def signal_handler(sender, instance, **kwargs):
    print("Signal handler executed")

def create_user():
    print("Creating user")
    with transaction.atomic():
        user = User.objects.create(username="testuser")
        print("User created")
if __name__ == "__main__":
    create_user()
    print("Done")
