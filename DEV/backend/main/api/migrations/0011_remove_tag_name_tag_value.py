# Generated by Django 4.1.2 on 2022-11-10 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0010_tag_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tag",
            name="name",
        ),
        migrations.AddField(
            model_name="tag",
            name="value",
            field=models.CharField(default="ES", max_length=3, unique=True),
        ),
    ]
