# Generated by Django 3.1.6 on 2021-02-04 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employees',
            fields=[
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]