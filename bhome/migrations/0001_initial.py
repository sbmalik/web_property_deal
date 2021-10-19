# Generated by Django 3.1.3 on 2020-11-22 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('rooms', models.IntegerField()),
                ('bath', models.IntegerField()),
                ('price', models.FloatField()),
                ('pic', models.ImageField(upload_to='')),
                ('garage', models.CharField(max_length=10)),
                ('shared', models.CharField(max_length=10)),
                ('bond', models.CharField(max_length=50)),
                ('available', models.CharField(max_length=122)),
                ('ow_email', models.EmailField(max_length=254)),
                ('ow_phone', models.CharField(max_length=122)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
