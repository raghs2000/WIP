# Generated by Django 2.2.7 on 2019-12-18 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventType', models.CharField(max_length=200)),
                ('eventName', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('eventScope', models.CharField(max_length=200)),
                ('dateCreated', models.DateTimeField(verbose_name='Date Created')),
                ('dateActive', models.DateTimeField(verbose_name='Date Active')),
                ('recurrence', models.CharField(max_length=200)),
            ],
        ),
    ]
