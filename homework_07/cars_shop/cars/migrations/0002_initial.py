# Generated by Django 4.2.3 on 2023-08-18 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelsGeneration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('body_type', models.CharField(choices=[('City car', 'City car'), ('Hatchback', 'Hatchback'), ('MPV', 'MPV'), ('Saloon', 'Saloon'), ('Coupe', 'Coupe'), ('Crossover', 'Crossover')], max_length=20)),
                ('engine_volume', models.DecimalField(decimal_places=1, max_digits=2)),
                ('engine_type', models.CharField(choices=[('gasoline', 'gasoline'), ('diesel', 'diesel'), ('electric', 'electric')], max_length=20)),
            ],
        ),
    ]