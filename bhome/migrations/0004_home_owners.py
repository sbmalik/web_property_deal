# Generated by Django 3.1.3 on 2020-11-22 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bhome', '0003_auto_20201122_0813'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='owners',
            field=models.BooleanField(default=False),
        ),
    ]
