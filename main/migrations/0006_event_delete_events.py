# Generated by Django 4.2.7 on 2024-03-04 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_events_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('username', models.CharField(max_length=25)),
                ('userID', models.IntegerField()),
                ('log_date', models.DateTimeField(verbose_name='date logged')),
            ],
            options={
                'db_table': 'tblevents',
            },
        ),
        migrations.DeleteModel(
            name='Events',
        ),
    ]