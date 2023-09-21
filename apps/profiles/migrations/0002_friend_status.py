# Generated by Django 4.2.5 on 2023-09-20 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='status',
            field=models.CharField(choices=[('pending', 'Ожидание'), ('accepted', 'Принято')], default='pending', max_length=10),
        ),
    ]
