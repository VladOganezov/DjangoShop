from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):

    order = Order.objects.get(id=order_id)
    subject = f'Заказ № {order.id}'
    message = f'Дорогой(ая) {order.first_name}, \n\n' \
              f'Ваш заказ успешно размещен. \n' \
              f'Номер заказа - {order.id}.'
    mail_sent = send_mail(subject,
                          message,
                          'admin@geekochad.com',
                          [order.email])
    return mail_sent