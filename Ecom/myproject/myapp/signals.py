from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in , user_logged_out , user_login_failed
from django.dispatch import receiver , Signal


save_signal = Signal()
