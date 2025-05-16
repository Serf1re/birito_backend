import uuid
from django.db import models
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings

EXECUTION = 'execution'
CANCELLED = 'cancelled'
COMPLETED = 'completed'
PENDING = 'pending'

class Order(models.Model):
    
    STATUS_CHOICES = [
        (EXECUTION, 'Выполняется'),
        (CANCELLED, 'Отменен'),
        (COMPLETED, 'Выполнен'),
        (PENDING, 'На рассмотрении')
    ]

    created = models.DateField(auto_now_add=True)
    title = models.CharField('Название заказа', max_length=100)
    description = models.TextField('Описание')
    status = models.CharField('Статус', max_length=10, choices=STATUS_CHOICES, default='pending')
    complete = models.BooleanField('Выполнен', default=False)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_owner', null=True, blank=True)
    executor_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_executor', null=True, blank=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title
    

class RegistrationLinks(models.Model):
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    used = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)

    
    def get_registration_link(self):
        domain = getattr(settings, 'SITE_DOMAIN', 'birito.ru')
        return f'https://{domain}/register/{self.token}'
    
    def __str__(self):
        return self.get_registration_link()+ " | " + f"Использовано: {self.used}"
