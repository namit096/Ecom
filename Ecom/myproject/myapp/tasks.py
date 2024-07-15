from celery import shared_task 
from myproject.celery import app
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings
from .models import Product, Variant, Categories

@app.task
def send_new_product_email(product_id):
    product = Product.objects.get(id=product_id)
    subject = 'New product added'
    message = f'{product.title}\n{product.description}'
    recipients = [user.email for user in User.objects.all() if user.email]
    send_mail(subject, message, settings.EMAIL_HOST_USER, recipients)

@app.task
def send_daily_status_email():
    print("Interogating the task")

    products_count = Product.objects.count()
    variants_count = Variant.objects.count()
    categories = Categories.objects.all()
    # categories_count = {category.title: category.product_set.count() for category in categories}
    customers_count = User.objects.filter(is_staff=False).count()

    subject = 'Daily Status Report'
    message = (
        f'Count of products: {products_count}\n'
        f'Count of variants: {variants_count}\n'
    )

    

    # for category, count in categories_count.items():
    #     message += f' - {category}: {count}\n'
    
    message += f'Number of customers: {customers_count}'

    staff_emails = [user.email for user in User.objects.filter(is_staff=True) if user.email]
    send_mail(subject, message, settings.EMAIL_HOST_USER, staff_emails)
