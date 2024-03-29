# Generated by Django 4.2.7 on 2024-03-03 14:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='log_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date logged'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='events',
            name='userID',
            field=models.IntegerField(default="1"),
            preserve_default=False,
        ),
    ]
