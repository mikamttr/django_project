# Generated by Django 5.0.1 on 2024-04-02 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0003_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]