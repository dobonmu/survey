# Generated by Django 4.2.5 on 2023-11-01 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0006_remove_question_photo_2"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="question",
            name="photo_1",
        ),
    ]