# Generated by Django 3.1.7 on 2021-05-13 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='desc',
            new_name='address',
        ),
        migrations.AddField(
            model_name='contact',
            name='DOB',
            field=models.DateField(default='', editable=False),
        ),
        migrations.AddField(
            model_name='contact',
            name='password',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='contact',
            name='roll',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=50),
        ),
    ]