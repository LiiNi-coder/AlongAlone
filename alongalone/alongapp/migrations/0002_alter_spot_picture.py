# Generated by Django 4.0.6 on 2022-07-22 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alongapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spot',
            name='picture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]