# Generated by Django 4.1.1 on 2022-10-28 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etudiants', '0008_dateheure_created_at_presence_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dateheure',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
