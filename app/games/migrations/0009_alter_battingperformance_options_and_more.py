# Generated by Django 4.1.7 on 2023-03-24 00:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("games", "0008_alter_battingperformance_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="battingperformance",
            options={"ordering": ("batted_at",)},
        ),
        migrations.AlterModelOptions(
            name="bowlingperformance",
            options={"ordering": ("bowled_at",)},
        ),
        migrations.AlterField(
            model_name="battingperformance",
            name="batted_at",
            field=models.IntegerField(
                choices=[
                    (0, 0),
                    (1, 1),
                    (2, 2),
                    (3, 3),
                    (4, 4),
                    (5, 5),
                    (6, 6),
                    (7, 7),
                    (8, 8),
                    (9, 9),
                    (10, 10),
                    (11, 11),
                ],
                default=0,
            ),
        ),
        migrations.AlterField(
            model_name="bowlingperformance",
            name="bowled_at",
            field=models.IntegerField(
                choices=[
                    (0, 0),
                    (1, 1),
                    (2, 2),
                    (3, 3),
                    (4, 4),
                    (5, 5),
                    (6, 6),
                    (7, 7),
                    (8, 8),
                    (9, 9),
                    (10, 10),
                    (11, 11),
                ],
                default=1,
            ),
        ),
    ]
