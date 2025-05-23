# Generated by Django 5.2.1 on 2025-05-16 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='name',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('execution', 'Выполняется'), ('cancelled', 'Отменен'), ('completed', 'Выполнен'), ('pending', 'На рассмотрении')], default='pending', max_length=10, verbose_name='Статус'),
        ),
    ]
