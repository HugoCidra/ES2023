# Generated by Django 4.1.2 on 2022-11-17 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0011_remove_tag_name_tag_value"),
    ]

    operations = [
        migrations.AddField(
            model_name="test",
            name="tags",
            field=models.ManyToManyField(to="api.tag"),
        ),
        migrations.AddField(
            model_name="test",
            name="title",
            field=models.CharField(default="", max_length=200),
        ),
    ]
