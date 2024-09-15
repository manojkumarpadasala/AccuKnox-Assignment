import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def slow_signal_handler(sender, instance, **kwargs):
    print("Signal received. Doing some work...")
    time.sleep(5)  # Simulate work
    print("Signal work done.")

def create_user():
    print("Creating user...")
    user = User.objects.create(username="testuser")
    print("User created.")

if __name__ == "__main__":
    create_user()
    print("Main thread done.")
