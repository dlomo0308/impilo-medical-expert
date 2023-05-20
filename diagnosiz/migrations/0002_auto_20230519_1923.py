# Generated by Django 3.1.1 on 2023-05-19 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cause',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Effect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='disease',
            name='causes',
        ),
        migrations.AddField(
            model_name='disease',
            name='effects',
            field=models.ManyToManyField(to='diagnosiz.Effect'),
        ),
        migrations.AddField(
            model_name='disease',
            name='causes',
            field=models.ManyToManyField(to='diagnosiz.Cause'),
        ),
    ]
