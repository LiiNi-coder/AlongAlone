# Generated by Django 4.0.4 on 2022-08-11 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communityapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(default='', max_length=10),
        ),
    ]