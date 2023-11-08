# Generated by Django 4.2.5 on 2023-11-02 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0013_remove_userresponse_open_answer"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userresponse",
            name="selected_choice",
        ),
        migrations.AddField(
            model_name="userresponse",
            name="selected_answer",
            field=models.IntegerField(default=0),
        ),
    ]
