# Generated by Django 4.1.5 on 2023-03-06 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogi', '0005_alter_postaus_kuva'),
    ]

    operations = [
        migrations.AddField(
            model_name='postaus',
            name='ingressi',
            field=models.TextField(blank=True),
        ),
    ]
