# Generated by Django 3.1.1 on 2023-06-04 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diagnosiz', '0002_auto_20230519_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cause',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='disease',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='effect',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='symptom',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.CreateModel(
            name='DiseaseDiagnosed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=254)),
                ('date_of_diagnosis', models.DateField()),
                ('diagnosed_disease', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]