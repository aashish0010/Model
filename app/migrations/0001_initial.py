# Generated by Django 3.1.7 on 2021-03-16 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=222)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=222)),
                ('phone', models.CharField(max_length=222)),
            ],
        ),
    ]