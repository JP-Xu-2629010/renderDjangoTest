# Generated by Django 5.0.6 on 2024-05-14 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tree01", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="usercase",
            name="cheaked",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (2, "2"), (3, "3")], default=0
            ),
            preserve_default=False,
        ),
    ]
