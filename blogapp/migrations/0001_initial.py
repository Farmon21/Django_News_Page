# Generated by Django 4.0.4 on 2022-05-14 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('descriptions', models.TextField()),
                ('img', models.ImageField(null=True, upload_to='')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
