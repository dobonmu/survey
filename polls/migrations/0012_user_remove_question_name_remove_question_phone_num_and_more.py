# Generated by Django 4.2.5 on 2023-11-02 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0011_question_name_question_phone_num"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("photo_1", models.CharField(max_length=200, null=True)),
                ("photo_2", models.CharField(max_length=200, null=True)),
                ("name", models.CharField(max_length=200, null=True)),
                ("phone_num", models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="question",
            name="name",
        ),
        migrations.RemoveField(
            model_name="question",
            name="phone_num",
        ),
        migrations.RemoveField(
            model_name="question",
            name="photo_1",
        ),
        migrations.RemoveField(
            model_name="question",
            name="photo_2",
        ),
        migrations.CreateModel(
            name="UserResponse",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "open_answer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="polls.open_answer",
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="polls.question"
                    ),
                ),
                (
                    "selected_choice",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="polls.choice",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="polls.user"
                    ),
                ),
            ],
        ),
    ]
