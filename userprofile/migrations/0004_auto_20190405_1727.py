# Generated by Django 2.1.7 on 2019-04-05 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20190321_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]