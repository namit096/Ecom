from django.dispatch import receiver
from myapp.signals import save_signal

@receiver(save_signal)
def handle_save_signal(sender ,mystring ,**kwargs):
    print(f'Printing the {mystring}')

# @receiver(user_logged_in)
# def user_logged_in_handler(sender , request , user , **kwargs):
#     print(f'User {user.username} logged in at ')