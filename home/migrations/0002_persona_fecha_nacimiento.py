# Generated by Django 4.1.1 on 2022-10-02 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
    ]
