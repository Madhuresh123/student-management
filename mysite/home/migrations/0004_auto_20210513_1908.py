# Generated by Django 3.1.7 on 2021-05-13 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210513_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]