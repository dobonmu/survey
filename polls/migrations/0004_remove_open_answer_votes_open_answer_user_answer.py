# Generated by Django 4.2.5 on 2023-10-28 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0003_remove_open_answer_choice_text_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="open_answer",
            name="votes",
        ),
        migrations.AddField(
            model_name="open_answer",
            name="user_answer",
            field=models.TextField(null=True),
        ),
    ]
