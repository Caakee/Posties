# Generated by Django 4.2.7 on 2024-03-04 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_event_delete_events'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='username',
            field=models.CharField(max_length=300),
        ),
    ]
