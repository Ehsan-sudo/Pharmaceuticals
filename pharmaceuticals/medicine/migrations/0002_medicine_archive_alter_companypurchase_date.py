# Generated by Django 4.0.6 on 2022-08-20 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='archive',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='companypurchase',
            name='date',
            field=models.DateField(),
        ),
    ]