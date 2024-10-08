# Generated by Django 4.2.7 on 2024-09-03 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("ageis_app", "0052_extendedusermodel_address_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="extendedusermodel",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="extendedusermodel",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="created_users",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="extendedusermodel",
            name="user_type",
            field=models.CharField(
                choices=[
                    ("owner", "Owner"),
                    ("manager", "Manager"),
                    ("staff", "Staff"),
                    ("user", "User"),
                ],
                default="user",
                max_length=10,
            ),
        ),
    ]
