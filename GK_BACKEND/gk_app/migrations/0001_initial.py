# Generated by Django 5.1 on 2024-08-22 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="super_admin_details",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=300)),
                ("password", models.CharField(max_length=300)),
                ("mobileNo", models.CharField(max_length=300)),
            ],
        ),
    ]
