# Generated by Django 4.0.6 on 2022-07-30 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='address_secret',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Address', models.CharField(max_length=10)),
                ('User_Secret', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='praise_tread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Address', models.CharField(max_length=10)),
                ('User_Comment', models.CharField(max_length=300)),
                ('User_Comment_Tread', models.CharField(max_length=1)),
                ('User_Comment_Praise', models.CharField(max_length=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='message',
            name='User_Comment_Praise',
        ),
        migrations.RemoveField(
            model_name='message',
            name='User_Comment_Tread',
        ),
    ]