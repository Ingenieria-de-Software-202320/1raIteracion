# Generated by Django 4.2.5 on 2023-10-11 22:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("records", "0008_shiftassignment_modified_at_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="shiftassignment",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="shiftassignment",
            name="modified_at",
        ),
        migrations.RemoveField(
            model_name="shiftassignment",
            name="modified_by",
        ),
        migrations.AddField(
            model_name="production",
            name="created_at",
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
        migrations.AddField(
            model_name="production",
            name="modified_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="production",
            name="modified_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="modified_shift_assignments",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]