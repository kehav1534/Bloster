# Generated by Django 4.2.9 on 2024-06-04 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("User", "0007_alter_userprofile_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="firstname",
            field=models.CharField(
                blank=True, default="user", max_length=35, verbose_name="First Name"
            ),
        ),
    ]
