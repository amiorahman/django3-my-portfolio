# Generated by Django 3.1.3 on 2020-12-15 15:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='date',
        ),
        migrations.AddField(
            model_name='gallery',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='gallery/images/'),
            preserve_default=False,
        ),
    ]
