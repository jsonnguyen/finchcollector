# Generated by Django 5.0.4 on 2024-04-24 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_hat'),
    ]

    operations = [
        migrations.AddField(
            model_name='finch',
            name='hats',
            field=models.ManyToManyField(to='main_app.hat'),
        ),
    ]
