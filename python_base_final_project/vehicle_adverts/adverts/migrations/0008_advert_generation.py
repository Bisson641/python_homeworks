# Generated by Django 4.2.3 on 2023-08-28 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0007_generation'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='generation',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='generations', to='adverts.generation'),
            preserve_default=False,
        ),
    ]
