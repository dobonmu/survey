# Generated by Django 4.2.5 on 2023-11-02 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0012_user_remove_question_name_remove_question_phone_num_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userresponse",
            name="open_answer",
        ),
    ]
