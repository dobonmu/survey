# Generated by Django 4.2.5 on 2023-11-01 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0007_remove_question_photo_1"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="photo_1",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="question",
            name="photo_2",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
