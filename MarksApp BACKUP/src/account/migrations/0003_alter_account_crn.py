# Generated by Django 4.2.5 on 2023-11-07 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_account_crn_account_subject_account_term'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='crn',
            field=models.IntegerField(default=0),
        ),
    ]
