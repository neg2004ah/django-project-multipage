# Generated by Django 4.1.7 on 2023-05-11 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertisModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='empty', max_length=100)),
                ('link', models.CharField(default='#', max_length=250)),
                ('image', models.ImageField(default='default.jpg', upload_to='images')),
            ],
        ),
    ]
