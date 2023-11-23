# Generated by Django 4.2.6 on 2023-11-22 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('venue_address', models.CharField(max_length=200)),
            ],
        ),
    ]
