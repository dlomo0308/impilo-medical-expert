# Generated by Django 3.1.1 on 2023-06-06 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosiz', '0005_auto_20230605_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnoseddisease',
            name='symptoms_selected',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]