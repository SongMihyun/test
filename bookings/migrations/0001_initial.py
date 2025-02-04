# Generated by Django 5.1.2 on 2024-10-16 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Booking",
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
                ("check_in_date", models.DateField()),
                ("check_out_date", models.DateField()),
                ("total_price", models.IntegerField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("confirmed", "Confirmed"),
                            ("paid", "Paid"),
                            ("partially_paid", "Partially Paid"),
                            ("check_in", "Checked In"),
                            ("check_out", "Checked Out"),
                            ("cancelled_by_guest", "Cancelled by Guest"),
                            ("cancelled_by_host", "Cancelled by Host"),
                            ("no_show", "No Show"),
                            ("refunded", "Refunded"),
                            ("completed", "Completed"),
                        ],
                        default="pending",
                        max_length=20,
                    ),
                ),
                ("request", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
