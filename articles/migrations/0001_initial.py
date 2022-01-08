# Generated by Django 3.2.11 on 2022-01-08 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_up', models.DateTimeField(auto_now_add=True)),
                ('updated_up', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]