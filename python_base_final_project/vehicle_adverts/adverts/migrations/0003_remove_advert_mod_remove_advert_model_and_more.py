# Generated by Django 4.2.3 on 2023-08-27 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0002_alter_advert_mod'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advert',
            name='mod',
        ),
        migrations.RemoveField(
            model_name='advert',
            name='model',
        ),
        migrations.RemoveField(
            model_name='advert',
            name='vehicle',
        ),
    ]
