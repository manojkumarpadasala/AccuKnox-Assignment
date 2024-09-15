import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Signal handler function
@receiver(post_save, sender=User)
def signal_handler(sender, instance, **kwargs):
    print(f"Signal handler thread ID: {threading.get_ident()}")

def create_user():
    print(f"Creating user in thread ID: {threading.get_ident()}")
    User.objects.create(username="testuser")

if __name__ == "__main__":
    print(f"Main thread ID: {threading.get_ident()}")
    create_user()
    print(f"Main thread ID after user creation: {threading.get_ident()}")
