# Generated by Django 5.1.4 on 2025-01-29 10:19

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("productApp", "0001_initial"),
        ("userApp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="addedby",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="userApp.profile",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="approved",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="product",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
