# Generated by Django 4.1.2 on 2022-11-24 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0017_alter_question_tag"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="solvedtest",
            unique_together={("user", "test")},
        ),
    ]
